from fractions import gcd

n, m = map(int, input().split())
s = input()
t = input()

gcd_nm = gcd(n, m)
ans = n * m // gcd_nm
n_tmp = n // gcd_nm
m_tmp = m // gcd_nm
for i in range(gcd_nm):
    if s[i * n_tmp] != t[i * m_tmp]:
        print(-1)
        break
else:
    print(ans)