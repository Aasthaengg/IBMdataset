### 解答
def popcount(X):
  pc = 0
  while X>0:
    pc += X%2
    X = X//2
  return pc

N = int(input())
B = input()
X = int(B, 2)

pcx = popcount(X)
pc0to1 = pcx + 1
pc1to0 = pcx - 1
if pc0to1 > 0:
  r0to1 = X%pc0to1
  r20to1 = [1]
  for i in range(1,N):
    r20to1.append((r20to1[-1]*2)%pc0to1)
if pc1to0 > 0:
  r1to0 = X%pc1to0
  r21to0 = [1]
  for i in range(1,N):
    r21to0.append((r21to0[-1]*2)%pc1to0)

for i in range(N):
  b = B[i]
  if b == "0":
    pc = pc0to1
  else:
    pc = pc1to0
  if pc == 0:
    print(0)
    continue

  if b == "0":
    x = r0to1 + r20to1[-(i+1)]
  else:
    x = r1to0 - r21to0[-(i+1)]
  x = x%pc

  ans = 1
  while x > 0:
    pc = popcount(x)
    x = x%pc
    ans += 1
  print(ans)

    
  

  


