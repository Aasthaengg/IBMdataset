def gcd(a, b):
    if a<b:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

a,b = list(map(int,input().split()))
c = gcd(a,b)
c0 = c
r = 2
lis = [1]
count = 1
while c != 1:
    if c%r == 0:
        c = c//r
        lis.append(r)
        r = 2
    else:
        r += 1
    if r > int(pow(c0,0.5))+1:
        lis.append(c)
        break
d = list(set(lis))
print(len(d))