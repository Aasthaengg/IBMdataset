N=int(input())
A=list(map(int,input().split()))
bef=99999999999999
count=0
max=0
for i in range(N):
  l=A.pop()
  if l >= bef:
    count +=1
  else:
    count=0
  if max <= count:
    max=count
  bef=l
print(max)
    
