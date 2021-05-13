n=int(input())
x=[]
ans=0
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a+b)
    ans-=b
x.sort(reverse=True)
ans+=sum(x[i] for i in range(n) if i%2==0)
print(ans)