import math
ans=[]
while True:
  n=int(input())
  if n==0:
    break
  S=list(map(int,input().split(' ')))
  mean=0

  for i in range(n):
    mean+=S[i]
  mean/=n

  a2=0
  for i in range(n):
   a2+=(S[i]-mean)**2

  a2/=n
  a=math.sqrt(a2)
  ans.append(a)


for i in range(len(ans)):
  print(ans[i])

