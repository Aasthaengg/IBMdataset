def main():
    import sys
    import heapq
    input = sys.stdin.readline
    N, C, K = [int(x) for x in input().strip().split()]
    T = []
    for _ in range(N):
        heapq.heappush(T, int(input()))
    
    k = 0
    c = 0
    ans = 0
    while T:
        t = heapq.heappop(T)
        if c % C == 0:
            k = t + K
            ans += (c > 0)
            c += 1
        elif t <= k:
            c += 1
        else:
            ans += 1
            c = 1
            k = t + K
    else:
        ans += (c > 0)

    print(ans)

if __name__ == '__main__':
    main()