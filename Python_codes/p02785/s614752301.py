n,k=map(int,input().split())
h=list(map(int,input().split()))

rh=sorted(h,reverse=True)
rh2=sum(rh[k:])

print(rh2)