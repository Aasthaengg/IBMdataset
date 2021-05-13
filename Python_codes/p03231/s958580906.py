from fractions import gcd
n,m = map(int, input().split())
s = input()
t = input()
# Xの長さLはnとmで割り切れる
# Xの1, L/n + 1, ..., (n-1) * L/n + 1 番目の文字をつなげるとSになる
# Xの1, L/m + 1, ..., (m-1) * L/m + 1 番目の文字をつなげるとTになる

ans = -1
if n==m:
    if s==t: ans= n
else:
    gcd_nm = gcd(n,m)
    for i in range(gcd_nm):
        if s[n//gcd_nm*i] != t[m//gcd_nm*i]: break
    else: ans = n*m//gcd_nm
print(ans)