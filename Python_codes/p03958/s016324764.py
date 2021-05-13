from sys import stdin

def main():
    import heapq
    input = stdin.readline
    input()
    a = [-1 * int(i) for i in input().split()]
    heapq.heapify(a)
    while len(a) > 1:
        u = heapq.heappop(a)
        v = heapq.heappop(a)
        if u + 1 < 0:
            heapq.heappush(a, u + 1)
        if v + 1 < 0:
            heapq.heappush(a, v + 1)
    if len(a) == 0:
        print(0)
    else:
        print(abs(a[0] + 1))
main()