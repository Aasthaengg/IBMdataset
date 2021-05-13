N=int(input())
A=list(map(int,input().split()))
B=sorted(A)
if N%2==1:
  D=[0]
  for i in range(N-1):
    D.append((i//2)*2+2)
  if B==D:
    print((2**((N-1)//2))%(10**9+7)) 
  else:
    print(0)
else:
  D=[(i//2)*2+1 for i in range(N)]
  if B==D:
    print((2**(N//2))%(10**9+7))
  else:
    print(0)