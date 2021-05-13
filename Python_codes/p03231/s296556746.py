[n,m] = list(map(int, input().split(" ")))
s = input()
t = input()
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
g = gcd(n,m)
out = n*m/g
for i in range (0,g):
    if s[i*int(n/g)] != t[i*int(m/g)]:
        out = -1
        break
print(int(out))