N, X = map(int, input().split())
m = [int(input()) for i in range(N)]
m.sort()
X -= sum(m)
print(int(N + X / m[0]))