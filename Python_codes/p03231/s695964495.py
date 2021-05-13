from fractions import gcd

n, m = map(int, input().split())

s = input()
t = input()

# accept
# a c p
# a  e

g = gcd(n, m)
a = n // g
b = m // g
for i in range(g):
    if s[i*a] != t[i*b]:
        print(-1)
        exit()

print(n*m//g)
