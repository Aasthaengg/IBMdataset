def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())
a = list(map(int,input().split()))
a = [a[i]//2 for i in range(n)]
l = 1
b = -1
for x in a:
    if l % x != 0:
        l = l * x // gcd(l,x)
    c = 0
    while x % 2 == 0:
        x = x // 2
        c += 1
    if b != -1 and b != c:
        print(0)
        exit()
    elif b == -1:
        b = c
        
ans = m // l
ans = (ans + 1) // 2
print(ans)
#print(l)
