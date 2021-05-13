N = int(input())
Stemp = str(input())
S = []
for i in range(N):
  temp = int(Stemp[i])
  S.append(temp)
ans = set([])
L = [[] for _ in range(10)]
for i in range(N):
  L[S[i]].append(i)
#print(L)
for v in range(1000):
  a = v//100
  b = (v-a*100)//10
  c = v-a*100-b*10
  if not L[a]:
    continue
  left = min(L[a])
  Flag = False
  for x in L[b]:
    if x > left:
      mid = x
      Flag = True
      break
  if not Flag:
    continue
  Flag = False
  for y in L[c]:
    if y > mid:
      right = y
      Flag = True
      break
  if not Flag:
    continue
  ans.add(v)
  #print(v,left,mid,right)
print(len(ans))        