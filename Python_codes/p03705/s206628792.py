N, A, B=map(int, input().split())
if N==1:
  if A==B:
    print(1)
  else:
    print(0)
else:
  if A>B:
    print(0)
  else:
    n=N-2
    ans=n*B-n*A+1
    print(ans)
