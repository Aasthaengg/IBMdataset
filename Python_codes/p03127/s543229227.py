def gcd(x,y):
    if x%y==0: return y
    else: return gcd(y,x%y)
n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = a[0]
for i in range(1,n):
    ans = min(ans,gcd(ans,a[i]))
print(ans)