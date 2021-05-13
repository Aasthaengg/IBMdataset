N = int(input())
if N%2==0:
  print(N*(N-2)//2)
  ans = []
  for i in range(1,N+1):
    for j in range(1,N+1):
      if i>=j or i+j==N+1:
        continue
      ans += [(i,j)]
  for a in ans:
    print(*a)
else:
  n = N-1
  print(n*(n-2)//2 + n)
  ans = []
  for i in range(1,n+1):
    for j in range(1,n+1):
      if i>=j or i+j==n+1:
        continue
      ans += [(i,j)]
  for a in ans:
    print(*a)
  for i in range(1,N):
    print(i,N)