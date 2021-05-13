N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

pow = X - sum(m)
mmin = min(m)
res = pow // mmin

print(N + res)