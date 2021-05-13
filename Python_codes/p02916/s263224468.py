n=int(input())
la=list(map(int,input().split()))
lb=list(map(int,input().split()))
lc=list(map(int,input().split()))

ans=sum(lb)
lt=[]
for i in range(len(la)-1):
  if la[i]+1==la[i+1]:
    lt.append(la[i])

for j in lt:
  ans+=lc[j-1]

print(ans)