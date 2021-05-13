from collections import deque

n = int(input())
ab = [list(map(int, input().split())) for i in range(n-1)]
c = sorted(list(map(int, input().split())), reverse = True)
tree = [list() for i in range(n)]
already = [1] * n 
ans = [0] * n
k = 0
queue = deque([0])

for index,(a,b) in enumerate(ab):
  a -= 1
  b -= 1
  tree[a].append((index,b))
  tree[b].append((index,a))
while queue:
  now = queue.popleft()
  already[now] = 0
  ans[now] = c[k]
  k += 1
  for index,i in tree[now]:
    if already[i]:
      queue.append(i)
         
print(sum(c[1:]))
print(*ans)
