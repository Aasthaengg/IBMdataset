from collections import deque
 
n = int(input())
a = list(map(int,input().split()))
d = deque(a)
 
tmp = []
cnt = 0
while d:
  v = d.popleft()
  if len(tmp)<=1:
    pass
  else:
    if not (v >= tmp[-1] >= tmp[-2] >= tmp[0] or v <= tmp[-1] <= tmp[-2] <= tmp[0]):
      tmp = []
      cnt += 1
  tmp.append(v)
#  print(d,tmp,cnt)
if tmp:
  cnt+=1
print(cnt)