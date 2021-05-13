_,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
temp=sum(a)
for v in a:
    if v>=temp/(4*m): cnt+=1
if cnt>=m: print("Yes")
else: print("No")