def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd (a, b) * b

n, m = map(int, input().split())
s = input()
t = input()

ans = lcm(n, m)

chk = {}

for i in range(n):
    d = ans//n
    chk[i*d] = s[i]
for i in range(m):
    d = ans//m
    if i*d in chk and chk[i*d] != t[i]:
        print(-1)
        exit()
print(ans)

