def gcd(a, b):
    if a<b:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
n = int(input())
a = list(map(int,input().split()))
ans = gcd(a[0],a[1])
for i in range(2,n):
    ans = gcd(ans,a[i])
print(ans)