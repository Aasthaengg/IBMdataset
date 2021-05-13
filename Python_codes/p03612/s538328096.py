N=int(input())
k=0
s=0
m=0
L=list(map(int,input().split()))
for i in range(N):
  if L[i]==i+1:
    m+=1
  else:
    s+=m//2+m%2
    m=0
s+=m//2+m%2
print(s)