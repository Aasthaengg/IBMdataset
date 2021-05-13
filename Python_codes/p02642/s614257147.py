def II(): return int(input())
def LI(): return list(map(int, input().split()))

N=II()
A=LI()
cnt=[0]*((10**6)+1)
for a in A:
  cnt[a]+=1
  
unique=[]
for i in range((10**6)+1):
  if cnt[i]==1:
    unique.append(i)
    
ans=0
cnt=[0]*((10**6)+1)
A=list(set(A))
for elem in A:
  for i in range(elem*2,(10**6)+1,elem):
    cnt[i]=1
for i in unique:
  if cnt[i]==0:
    ans+=1
print(ans)