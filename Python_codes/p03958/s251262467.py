k,t=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
tmp=a[-1]-1-sum(a[:-1])
if tmp>=0:
    print(tmp)
else:
    print(0)