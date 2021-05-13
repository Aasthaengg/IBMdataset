n , p = map(int, input().split())
a = list(map(int,input().split()))
b = [0]*n

for i in range(n):
    b[i]=a[i]%2

ans=2**(n-1)
if p==1 and sum(b)==0:
    ans = 0
if p==0 and sum(b)==0:
    ans *= 2
print(ans)
