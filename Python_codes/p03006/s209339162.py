N=int(input())
if N==1:
  print(1)
  exit()
  
A=[list(map(int,input().split())) for i in range(N)]
B={}
for a,b in A:
  for c,d in A:
    e=a-c
    f=b-d
    if e!=0 or f!=0:
      if (e,f) in B:
        B[(e,f)]+=1
      else:
        B[(e,f)]=1
a=max(B.values())
print(N-a)