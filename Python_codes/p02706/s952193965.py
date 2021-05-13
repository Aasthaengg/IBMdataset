n, m = map(int, input().split())
d = list(map(int, input().split()))

if n - sum(d) <= -1:
    print(-1)
else:
    print(n - sum(d))