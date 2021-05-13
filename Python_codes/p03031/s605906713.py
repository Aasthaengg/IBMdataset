n,m=map(int,input().split())
K=[]
S=[]
for i in range(m):
  tmp=list(map(int,input().split()))
  K.append(tmp[0])
  S.append(tmp[1:])
P=list(map(int,input().split()))
ans=0
for i in range(2**n):
  bit=format(i,'0'+str(n)+'b')
  bit=list(map(int,bit))
  on_den=0
  for den in range(m):
    on_swi=0
    for s in S[den]:
      on_swi+=bit[s-1]
    if on_swi%2==P[den]:
      on_den+=1
  if on_den==m:
    ans+=1
print(ans)