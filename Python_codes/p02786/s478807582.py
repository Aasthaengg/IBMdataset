#aのn乗を計算
def pow(a,n):
  if n==0:
    return 1
  else:
    k=pow(a*a,n//2)
    if n%2==1:
      k=k*a
  return k

h=int(input())
cnt=0
while h>1:
  h=h//2
  cnt=cnt+1
  
print(2*pow(2,cnt)-1)
