N, A, B = map(int, input().split())
if A==0:
  print(0)
  exit(0)

x = N//(A+B)
y = (N - x*(A+B))
blue=x*A + (A if y>=A else y%A)
print(blue)