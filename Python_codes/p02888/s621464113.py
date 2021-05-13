n = int(input())
l = sorted(map(int, input().split()))
cnt = 0
m = n-1
g = []
for i in range(n):
  for j in range(i):
    g.append(l[i]+l[j])
g = sorted(g,reverse = True)
for i in g:
  while l[m] >= i:
    m-=1
  cnt += n-m-1
print(n*(n-1)*(n-2)//6-cnt)