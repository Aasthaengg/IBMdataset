MM = input().split()
D = int(MM[0])
N = int(MM[1])
if N ==100:
  ans = 100**D*(N+1)
else:
  ans = 100**D *N
print(ans)