pre=-1
n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
cl=[0]+list(map(int,input().split()))
ans=0
prec=0
for  a,b in zip(al,bl):
    ans+=b
    if pre+1==a:ans+=cl[pre]
    pre=a
print(ans)