def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b,k = map(int,input().split())
r = gcd(a,b)
e = []
for i in range(1,r+1):
    if r%i == 0:
        e.append(i)
print(e[len(e)-k])