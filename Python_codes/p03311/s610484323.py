# 2019/08/13

n=int(input())
a=list(map(int,input().split()))

amin=float('inf')
for i in range(n):
    a[i]-=i+1

a.sort()
b=a[n//2]
ans=0
for e in a:
    ans+=abs(e-b)
print(ans)