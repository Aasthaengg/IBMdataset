n,l=map(int,input().split())
a=[i for i in range(l,l+n)]
if l>=0:
    eat=min(a)
elif l+n>0:
    eat=0
elif l+n<=0:
    eat=max(a)
    
print(sum(a)-eat)