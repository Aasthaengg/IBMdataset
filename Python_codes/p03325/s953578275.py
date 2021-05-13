n=int(input())
a=list(map(int,input().split()))

def count(x):
    res=0
    while x%2==0:
        res+=1
        x=x//2
    return res
ans=0
for i in range(n):
    ans+=count(a[i])

print(ans)