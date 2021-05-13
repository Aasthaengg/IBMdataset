N, X = map(int, input().split())
d = [int(input()) for i in range(N)]
a=(X-sum(d))//min(d)
print(N+a)

