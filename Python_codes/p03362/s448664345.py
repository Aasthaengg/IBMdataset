n=int(input())

fact=[True]*55556
fact[0]=False
fact[1]=False
ans=[]
for i in range(2,len(fact)):
  if fact[i]:
    if i%5==1:
      ans+=[i]
      if len(ans)==n:
        print(*ans)
        break
    for j in range(i*2,len(fact),i):
      fact[j]=False
