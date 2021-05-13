N,K = map(int, input().split())
if K > (N-1)*(N-2)//2:
  print(-1)
  exit(0)
ANS = []
for i in range(2,N+1):
  ANS.append((1,i))
  
cnt = (N-1)*(N-2)//2
for i in range(2,N+1):
  if cnt == K:
    break
  for j in range(i+1,N+1):
    ANS.append((i,j))
    cnt -= 1
    if cnt == K:
      break
      
print(len(ANS))
for i,j in ANS:
  print(i,j)