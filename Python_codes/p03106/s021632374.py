a,b,k=map(int,input().split())

cnt=0
s=min(a,b)

for i in range(s,0,-1):
  if a%i==0 and b%i==0:
    cnt+=1
    #print(i)
    if cnt==k:
      print(i)
      exit()
