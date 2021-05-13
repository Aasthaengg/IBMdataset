def keta_sum(n):
  sum = 0
  while n>0:
      sum += n%10
      n = n//10
  return(sum)

N,A,B=map(int,input().split())
sum=0
for i in range(1,N+1) :
  n=keta_sum(i)
  if A<=n and n<=B :
    sum+=i
print(sum)