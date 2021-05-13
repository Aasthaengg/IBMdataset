N = int(input())
As = list(map(int,input().split()))
Bs = list(map(int,input().split()))

Cs = []

if sum(As) < sum(Bs):
  print(-1)
  exit()

cnt = 0
ms = 0
ps = 0
for i in range(N):
  Cs.append(As[i]-Bs[i])
  if As[i]-Bs[i] < 0:
    cnt += 1
    ms += Bs[i] - As[i]
    
if cnt == 0:
  print(cnt)
  exit()
  
Cs.sort()
i = 0
while ps < ms:
  i += 1
  ps += Cs[-i]
  
print(cnt+i)