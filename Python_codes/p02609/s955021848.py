N = int(input())
X = input()
ans = [1 for _ in range(N)]

if N == 1:
  if X[0] == '1':
    print(0)
    exit()
  else:
    print(1)
    exit()
 
l = 0
for k in range(N):
  if X[k] == '1':
    l+=1

if l == 0:
  for _ in range(N):
    print(1)
  exit()
if l == 1:
  if X[-1] == '1':
    for _ in range(N-1):
      ans[_] = 2
  else:
    ans[-1] = 2 
  for k in range(N):
    if X[k] =='1':
      ans[k] = 0 
  for _ in range(N):
    print(ans[_])
  exit()
 
 
intN = int(X, 2)
N1 = intN %(l-1)
N0 = intN %(l+1)


start = []
s1 = 1
s0 = 1
for k in range(N-1, -1, -1):
  if X[k] == '1':      
    ia = (N1 - s1)%(l-1)
  else:
    ia = (N0 + s0)%(l+1)
  start.append(ia)
  s1 = s1*2%(l-1)
  s0 = s0*2%(l+1)
start = start[::-1]

ml = len(bin(l+1))-2
poplist = [[] for _ in range(ml)]
poplist[0] = [0,1]
for k in range(1, ml):
  for m in range(k):
    poplist[k] += poplist[m]
  for m in range(len(poplist[k])):
    poplist[k][m] += 1
newpoplist = []
for _ in range(len(poplist)):
  newpoplist += poplist[_] 


for k in range(len(start)):
  for count in range(10*5):
    if start[k] == 0:
      ans[k] += count
      break
    else:
      start[k] = start[k] % newpoplist[start[k]]
 
for k in range(N):
  print(ans[k])