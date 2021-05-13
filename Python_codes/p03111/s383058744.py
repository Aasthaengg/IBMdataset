n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
ans = 10**6
for i in range(4**n):
  pattern = [0]*n
  for j in range(n):
    pattern[j] = ((i >> j*2) & 3)
  bamboo = [0]*4
  for j in range(n):
    bamboo[pattern[j]] += l[j]
  if bamboo[1]*bamboo[2]*bamboo[3]==0:
    continue
  time = pattern.count(1)*10+pattern.count(2)*10+pattern.count(3)*10-30+abs(bamboo[1]-a)+abs(bamboo[2]-b)+abs(bamboo[3]-c)
  if ans > time:
    ans = time
print(ans)