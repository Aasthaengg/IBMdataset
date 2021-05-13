def main():
    import sys
    from collections import defaultdict
    from heapq import heappop, heappush
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    used = defaultdict(int)
    tank = []
    
    p = []
    p_append = p.append
    for i in range(N):
        s, t, x = map(int, input().split())
        p_append((s - x, x))
        p_append((t - x, -x))
    p.sort()

    cnt = 0
    for i in range(Q):
        d = int(input())
        while cnt <= len(p) - 1 and p[cnt][0] <= d:
            w = p[cnt][1]
            if w >= 0:
                used[w] += 1
                heappush(tank, w)
            else:
                used[-w] -= 1
            cnt += 1
        while True:
            if len(tank) == 0:
                print (-1)
                break
            kouho = tank[0]
            if used[kouho] > 0:
                print (kouho)
                break
            else:
                heappop(tank)

if __name__ == '__main__':
    main()