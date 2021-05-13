N = int(input())
B = list(map(int,input().split()))

ans = []
while N > 0:
  ok = False
  for i in range(N)[::-1]:
    b = B[i]
    if b == (i+1):
      ans.append(b)
      ok = True
      k = i
      break
  
  if not ok:
    break
  else:
    newB = []
    for i in range(N):
      if i != k:
        newB.append(B[i])
    
    B = newB
    N -= 1

if N != 0:
  print(-1)
else:
  print("\n".join(map(str,ans[::-1])))
