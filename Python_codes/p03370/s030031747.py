N, X = map(int,input().split())
m = [int(input()) for _ in range(N)]
X -= sum(m)
a = min(m)
print(N + X//a)
