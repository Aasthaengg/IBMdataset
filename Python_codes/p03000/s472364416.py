N,X=map(int,input().split())
L=list(map(int,input().split()))

x=0
count=1
for i in range(N):
  x += L[i]
  if x > X:break
  count+=1
print(count)