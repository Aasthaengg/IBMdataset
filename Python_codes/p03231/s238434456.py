n,m = list(map(int, input().split()))
s = input()
t = input()
import math

# 良い文字列が作れるなら、答えはLCM(n, m)となる
lcm = n * m // math.gcd(n, m)

x = {}
for i,c in enumerate(s):
    # (pos, char)
    x[lcm//n*i] = c

for i,c in enumerate(t):
    # (pos, char)
    pos, char = lcm//m*i, c
    if pos in x and x[pos] != char:
        print(-1)
        exit()

print(lcm)