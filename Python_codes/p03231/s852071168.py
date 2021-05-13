from math import gcd
n,m = map(int,input().split())
z = n * m // gcd(n,m)
s = input()
t = input()
n = z // n
m = z // m
x = 0
y = 0
i = 0
j = 0
while x < z and y < z:
    if x > y:
        y += m
        j += 1
    elif x < y:
        x += n
        i += 1
    else:
        if s[i] != t[j]:
            print(-1)
            exit(0)
        x += n
        y += m
        i += 1
        j += 1
print(z)