N = int(input())
A = list(map(int,input().split()))
A.sort()
mida = A[N//2-1]
midb = A[N//2]
if mida == midb:
  print(0)
else:
  ans = midb-mida
  print(ans)
