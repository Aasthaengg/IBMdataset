n=int(input())
ab=[]
sumb=0
for _ in range(n):
    a,b=map(int,input().split())
    ab.append(a+b)
    sumb+=b
ab.sort(reverse=True)
ans=0
for i in range(n):
    if i%2==0:
        ans+=ab[i]
print(ans-sumb)