N,M=list(map(int,input().split()))
L=list(map(int,input().split()))
if N not in L:
  print(N)
  exit()
c=N
d=N
while True:
  if c not in L:
    break
  else:
    c-=1
while True:
  if d not in L:
    break
  else:
    d+=1
if abs(d-N)>=abs(c-N):
  print(c)
else:
  print(d)