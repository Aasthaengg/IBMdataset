def calc(b,A):
  ret=0
  for i,num in enumerate(A):
    ret += abs( num-(b+i+1) )
  return ret    
##########################

N=int(input())
A=list(map(int,input().split()))

L=-1*10**9
R=10**9
i=(L+R)//2

while True:
  s=calc(i-1,A)
  t=calc(i,A)
  u=calc(i+1,A)
  if s<t<u:
    R=i
    i=(L+R)//2
  elif s>t>u:
    L=i
    i=(L+R)//2
  else:
    print(t)
    break