import sys
N,M = map(int,input().split())
cc = [list(map(int, input().split())) for i in range(M)]
if [1,0] in cc:
  if N!= 1:
    print(-1)
    sys.exit()
a,b = [0]*N,['v']*N
for [i,j] in cc:
  a[i-1] = j
  if b[i-1] != 'v' and b[i-1] != j:
    print(-1)
    sys.exit()
  b[i-1] = j
if a[0] == 0:
  if N != 1:
    a[0] = 1
c = ''
for i in a:
  c = c + str(i)
print(c)