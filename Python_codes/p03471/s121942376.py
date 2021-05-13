N,Y = map(int,input().split())

Y //= 1000
res = [-1,-1,-1]

for i in range(N+1):
  remN = N-i
  remY = Y - 10*i
  if remY < 0:
    break
  for j in range(remN+1):
    if remY - 5*j == remN - j:
      res = [i,j,N-i-j]
      
print(" ".join(map(str,res)))