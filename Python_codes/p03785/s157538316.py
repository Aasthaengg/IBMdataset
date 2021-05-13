n,c,k=map(int,input().split())
t=sorted([int(input()) for _ in range(n)])
bc=[1]
bt=[t[0]+k]
for i in range(1,n):
  if bc[-1]<c and t[i]<=bt[-1]<=t[i]+k:bc[-1]+=1
  else:
    bc+=[1]
    bt+=[t[i]+k]
print(len(bt))