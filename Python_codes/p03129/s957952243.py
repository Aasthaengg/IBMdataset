N,K=map(int,input().split())

if N%2==0:
  if K<=N//2:
    print("YES")
  else:
    print("NO")
else:
  if K<=(N+1)//2:
    print("YES")
  else:
    print("NO")