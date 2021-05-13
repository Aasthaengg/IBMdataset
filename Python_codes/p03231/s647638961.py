def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, m = map(int, input().split())
s = input()
t = input()
gcd_nm = gcd(n, m)
for i in range(gcd_nm):
    if s[i * n // gcd_nm] != t[i * m // gcd_nm]:
        print(-1)
        break
else:
    print(n*m//gcd_nm)