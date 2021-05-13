def main():
    from collections import deque


    INF = float('inf')
    n, m = map(int, input().split())
    s = list(map(int, input()))

    dp = [INF] * (n + 1)
    dp[n] = 0
    queue = deque([0])

    i = n - 1
    while i >= 0:
        while True:
            if not queue:
                print(-1)                
                return            
            if queue[0] != INF and len(queue) <= m:
                break
            queue.popleft()
            
        if s[i] == 0:
            dp[i] = queue[0] + 1
        queue.append(dp[i])
        i -= 1

    ans = []
    v = dp[0]
    num = 0
    for i in dp:
        if i != v and i != INF:
            ans.append(num)
            v = i
            num = 1
        else:
            num += 1

    print(*ans, sep=' ')


if __name__ == '__main__':
    main()    