N=int(input())
m=0
maxa=-1
L=list(map(int,input().split()))
for i in range(N-1):
  if L[i]>=L[i+1]:
    m+=1
  else:
    maxa=max(maxa,m)
    m=0
maxa=max(maxa,m)
print(maxa)