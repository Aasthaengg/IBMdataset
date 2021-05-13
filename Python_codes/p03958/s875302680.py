k,t=map(int,input().split())
a=list(map(int,input().split()))
if t==1: print(a[0]-1)
else:
    temp=max(a)
    rest=sum(a)-temp
    if rest>=temp-1: print(0)
    else: print(temp-rest-1)