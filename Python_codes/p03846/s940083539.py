MOD=1000000007
N=int(input())
A=sorted(list(map(int,input().split())))
m=N%2
if m==1 and A[0]!=0:
  print(0)
else:
  for i in range(N//2):
    if A[2*i+m]==A[2*i+1+m]==2*i+1+m:
      continue
    else:
      print(0)
      exit()
  print(2**(N//2)%MOD)