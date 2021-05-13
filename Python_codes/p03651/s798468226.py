def gcd(a, b):
    if a<b:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
def gcd_all(A):
    x = A[0]
    if len(A) == 1:
        ret = A[0]
    else:
        for i in range(1,len(A)):
            x = gcd(x,A[i])
        ret = x
    return ret

n,k = map(int,input().split())
a = list(map(int,input().split()))
x = gcd_all(a)
ans = 0
for b in a:
    if b >= k:
        if (b-k)%x == 0:
            ans = 1
            break
print(["IMPOSSIBLE","POSSIBLE"][ans])