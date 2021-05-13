N=int(input())
lis=[0]*(N+10)
i=1

while i<=N:
  if i%3!=0 and i%5!=0:
    lis[i]=i
  i+=1
print(sum(lis))