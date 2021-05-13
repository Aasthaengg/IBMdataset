n, m = map(int, input().split())
s = input()
t = input()
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
g = gcd(n, m)
l = n*m//g
for i, j in zip(s[0:n:n//g], t[0:m:m//g]):
    if i!=j:
        print(-1)
        break
else:
    print(l)