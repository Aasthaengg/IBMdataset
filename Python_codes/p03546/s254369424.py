h,w = map(int,input().split())
c = []
for i in range(10):
  ci = list(map(int,input().split()))
  c.append(ci)
x = [0 for _ in range(10)]
for _ in range(h):
  a = list(map(int,input().split()))
  for ai in a:
    if ai != -1:
      x[ai] += 1
d = [float("inf") for _ in range(10)]
d[1] = 0
done = [False for _ in range(10)]
while sum(done) < 10:
  mni = -1
  mn = float("inf")
  for i in range(10):
    if done[i] == False:
      if mn > d[i]:
        mn = d[i]
        mni = i
  done[mni] = True
  for i in range(10):
    if done[i] == False:
      d[i] = min(d[i],d[mni]+c[i][mni])
ans = 0
for i in range(10):
  ans += x[i]*d[i]
print(ans)