n=int(input())
*a,=map(int,input().split())
a=sorted(a,reverse=True)
ans=0
for i in range(n-1):
    ans+=a[(i+1)//2]
print(ans)