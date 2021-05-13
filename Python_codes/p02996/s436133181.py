N = int(input())
C = {}

for i in range(N):
  a, b = map(int,input().split())
  if b in C.keys():
    C[b] += a
  else:
    C[b] = a
    
time = 0
D = sorted(C.items())

for i in range(len(D)):
  time += D[i][1]
  if time > D[i][0]:
    print('No')
    break
else:
  print('Yes')


