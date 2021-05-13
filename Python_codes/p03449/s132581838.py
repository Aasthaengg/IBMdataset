from collections import deque

def main():
    n=int(input())
    a=[tuple(map(int,input().split())) for _ in range(2)]
    dp=[[0]*n for _ in range(2)]
    dp[0][0] = a[0][0]
    q = deque([(0,0)])
    while len(q) > 0:
        cur = q.popleft()
        #print("cur", cur)
        for s in nextstep(cur, n):
            #print(s, end="")
            dp[s[0]][s[1]] = max(dp[s[0]][s[1]], dp[cur[0]][cur[1]]+a[s[0]][s[1]])
            q.append(s)
            #print(dp)
    print(dp[-1][-1])

def nextstep(cur, m):
    if cur[0] == 0:
        yield (1, cur[1])
    if cur[1] < m-1:
        yield (cur[0], cur[1] + 1)

if __name__ == "__main__":
    main()