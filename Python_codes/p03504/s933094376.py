def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    n, c = map(int, input().split())
    channels = [[] for _ in range(c)]
    for _ in range(n):
        i, j, k = map(int, input().split())
        channels[k-1].append([i, j])

    programs = []
    for channel in channels:
        if channel == []:
            continue

        channel.sort()
        for i in range(len(channel)-1):
            if channel[i][1] == channel[i+1][0]:
                channel[i+1][0] = channel[i][0]
            else:
                programs.append(channel[i])
        programs.append(channel[-1])

    programs.sort()

    from heapq import heappushpop, heappush

    heap = [programs[0][1]]
    for i in range(1, len(programs)):
        if heap[0] < programs[i][0]:
            heappushpop(heap, programs[i][1])
        else:
            heappush(heap, programs[i][1])
    
    print(len(heap))

main()