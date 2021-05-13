import sys

def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = [0] + LS2()
n = len(S)
mod = 10**9+7

a,c,d = [0]*n,[0]*n,[0]*n  # a[i],c[i],d[i] = S1~SiにあるA,C,?の個数
for i in range(1,n):
    a[i] = a[i-1]
    c[i] = c[i-1]
    d[i] = d[i-1]
    if S[i] == 'A':
        a[i] += 1
    elif S[i] == 'C':
        c[i] += 1
    elif S[i] == '?':
        d[i] += 1

X = [1]  # X[i] = 3**i
for _ in range(n):
    X.append((X[-1]*3) % mod)

hatena = d[n-1]  # Sにある?の個数

ans = 0
for i in range(1,n):
    if S[i] == 'B':
        ans += a[i-1]*(c[n-1]-c[i])*X[max(hatena,0)]
        ans %= mod
        ans += a[i-1]*(d[n-1]-d[i])*X[max(hatena-1,0)]
        ans %= mod
        ans += d[i-1]*(c[n-1]-c[i])*X[max(hatena-1,0)]
        ans %= mod
        ans += d[i-1]*(d[n-1]-d[i])*X[max(hatena-2,0)]
        ans %= mod
    elif S[i] == '?':
        ans += a[i-1]*(c[n-1]-c[i])*X[max(hatena-1,0)]
        ans %= mod
        ans += a[i-1]*(d[n-1]-d[i])*X[max(hatena-2,0)]
        ans %= mod
        ans += d[i-1]*(c[n-1]-c[i])*X[max(hatena-2,0)]
        ans %= mod
        ans += d[i-1]*(d[n-1]-d[i])*X[max(hatena-3,0)]
        ans %= mod

print(ans)
