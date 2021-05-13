N = int(input())
A = list(map(int,input().split()))

MAXN = N+1
p = 10**9+7
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % p)
def nCr(n, r, mod=p):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

MA = max(A)
out = [MA,0]
MA2 = MA//2
mincand = 10**9
for i in range(N):
    if mincand>abs(A[i]-MA2) and A[i]!=MA:
        mincand = abs(A[i]-MA2)
        out[1] = A[i]
print(*out)