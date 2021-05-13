N = int(input())
D = [[0]*10 for i in range(10)]
for n in range(1, N+1):
  s = str(n)
  i = int(s[0])
  j = int(s[-1])
  D[i][j] += 1
#print(D)
r = 0
for i in range(10):
  for j in range(10):
    r += D[i][j]*D[j][i]
print(r)
