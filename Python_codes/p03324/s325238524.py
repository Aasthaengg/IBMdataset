D, N = map(int, input().split())
ans = 0
df = 0

if D == 0:
    df = 1
elif D == 1:
    df = 100**1
else:
    df = 100**2

if N < 100:
    ans = df * N
else:
    ans = df * (N+1)

print(ans)