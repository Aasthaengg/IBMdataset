h,w=map(int,input().split())
a=[input() for _ in range(h)]
seen=[[-1]*w for _ in range(h)]
from collections import deque
todo=deque([])
for hi in range(h):
  for wi in range(w):
    if a[hi][wi]=='#':
      seen[hi][wi]=0
      todo.append((hi,wi,0))
while len(todo)>0:
  hi,wi,i=todo.popleft()
  if hi>0 and seen[hi-1][wi]==-1:
    todo.append((hi-1,wi,i+1))
    seen[hi-1][wi]=i+1
  if hi<h-1 and seen[hi+1][wi]==-1:
    todo.append((hi+1,wi,i+1))
    seen[hi+1][wi]=i+1
  if wi>0 and seen[hi][wi-1]==-1:
    todo.append((hi,wi-1,i+1))
    seen[hi][wi-1]=i+1
  if wi<w-1 and seen[hi][wi+1]==-1:
    todo.append((hi,wi+1,i+1))
    seen[hi][wi+1]=i+1
print(max([max(seeni) for seeni in seen]))
