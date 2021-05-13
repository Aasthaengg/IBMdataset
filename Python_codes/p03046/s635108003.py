m,k = map(int,input().split())
if m == 1 and k == 0:
  print("0 0 1 1")
  quit()
n=2**m
k += (n == 2 and k == 1)
p=list(range(n))
print(" ".join([str(t) for t in p[:k]+p[k::-1]+p[:k:-1]+p[k:]]) if k<n else -1)
