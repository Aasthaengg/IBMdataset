H, W, K = map(int, input().split())
S = []
for _ in range(H):
  S.append(input())
hsummation = [[int(S[0][k])]for k in range(W)]
for k in range(W):
  for j in range(1, H):
    hsummation[k].append(hsummation[k][j-1] + int(S[j][k]))

ans = float('inf')
anskouho = 0
h = -1
binhh = []
for j in range(2**(H-1)):
  h += 1
  binh = "0"*(H-len(str(bin(h)))+1)+str(bin(h))[2:]
  c = 0
  for k in range(len(binh)):
    if binh[k] == '1':
      c += 1
  binhh.append([binh, c])
binhh.sort(key = lambda x:x[1] , reverse= True)

for j in range(2**(H-1)):
  hlist=[]
  for k in range(H-1):
    if binhh[j][0][k] == '1':
      hlist.append(k)
  hlist.append(-1)
  anskouho = len(hlist)-1
  now = 0
  while now < W:
    counter = [0 for _ in range(len(hlist))]
    while now < W:
      counter[0] += hsummation[now][hlist[0]]
      if counter[0] > K:
        anskouho += 1
        break
      for l in range(1, len(hlist)):
        counter[l] += - hsummation[now][hlist[l-1]] + hsummation[now][hlist[l]]
        if counter[l] > K:
          anskouho += 1
          break
      else:
        now += 1
        continue
      break
    if anskouho > ans:
      break
  else:
    ans = anskouho
print(ans)