K,T=map(int,input().split())
A=list(map(int,input().split()))
if K%2==0:
  a=K//2
  b=max(A)
  if a>=b:
    print(0)
  else:
    print((b-a)*2-1)
else:
  a=K//2+1
  b=max(A)
  if a>=b:
    print(0)
  else:
    print((b-a)*2)