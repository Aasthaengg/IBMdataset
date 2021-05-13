N, K = map(int, input().split())
A = list(map(int, input().split()))
ndict = {i:0 for i in range(1, N+1)}
for i in A:
  ndict[i] += 1

nndict = {}
nnlist = []
for i in range(1, N+1):
  if ndict[i] >= 1:
    if ndict[i] not in nndict:
      nndict[ndict[i]] = 1
      nnlist.append(ndict[i])
    else:
      nndict[ndict[i]] += 1
      
nnlist.sort(reverse=True)


ki = K
for i in range(len(nnlist)):
  if ki > nndict[nnlist[i]]:
    ki -= nndict[nnlist[i]]
  else:
    nndict[nnlist[i]] -= ki
    inow = i
    break
else:
  print(0)
  exit()

ans = 0
for i in range(i, len(nnlist)):
  ans += nndict[nnlist[i]] * nnlist[i]
print(ans)