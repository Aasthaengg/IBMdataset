N,W = map(int,input().split())
w1,v1 = map(int,input().split())
items = {w: [] for w in range(w1,w1+4)}
items[w1].append(v1)

if N==1:
  print(v1)
  exit()

for _ in range(N-1):
  w,v = map(int,input().split())
  items[w].append(v)

lens = {}
for key in sorted(items.keys()):
  items[key].sort(reverse=True)
  lens[key] = len(items[key])

ans = -float('inf')
for i1 in range(lens[w1]+1):
  for i2 in range(lens[w1+1]+1):
    for i3 in range(lens[w1+2]+1):
      if W-i1*w1-i2*(w1+1)-i3*(w1+2) < 0: continue
      i4 = (W-i1*w1-i2*(w1+1)-i3*(w1+2))//(w1+3)
      ans = max(ans, sum(items[w1][:i1])+sum(items[w1+1][:i2])+sum(items[w1+2][:i3])+sum(items[w1+3][:i4]))
print(ans)