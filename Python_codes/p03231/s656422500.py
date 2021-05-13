import math

n, m = map(int,input().split())
s = input()
t = input()

x = math.gcd(n,m)
ans = n*m//x
n = n//x
m = m//x

for i in range(x):
    if s[n*i] != t[m*i]:
        print(-1)
        exit()

print(ans)