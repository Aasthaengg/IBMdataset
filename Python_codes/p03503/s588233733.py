from itertools import product

N=int(input())
F=[ [[0 for _ in range(2)] for _ in range(5)] for _ in range(N)]
P= [[0] for _ in range(N)]
total= [[0 for _ in range(5)] for _ in range(2)]

for i in range(N):
  tmp=list( map(int,input().split()) )
  for j in range(5):
    for k in range(2):
      F[i][j][k]=tmp[2*j+k]
for i in range(N):
  P[i]=list(map(int,input().split()))
  
maxi=float("-inf")
combi=product([1,0],repeat=10)

for kumi in combi:
  mini=float("-inf")
  if sum(kumi)==0:
    pass
  else:      
    tmp=0
    for i in range(N):
      summ=0
      for k,open in enumerate(kumi):
        m,n = k//2, k%2
        summ += open * F[i][m][n]
      tmp += P[i][summ]
  maxi=max(maxi,tmp)
      
print(maxi)