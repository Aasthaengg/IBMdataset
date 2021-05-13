n,m = list(map(int, input().split()))
s = input()
t = input()
import math

# 良い文字列が作れるなら、答えはLCM(n, m)となる
gcd = math.gcd(n, m)
if s[::n//gcd] == t[::m//gcd]:
    print(n * m // gcd)
else:
    print(-1)