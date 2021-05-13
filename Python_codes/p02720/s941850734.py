K = int(input())

from collections import deque
d = deque()
for i in range(1,10):
  d.append(str(i))

for _ in range(K):
  a = d.popleft()
  #print(a)
  if a[-1] != '0':
    d.append(a+str(int(a[-1])-1))
  d.append(a+a[-1])
  if a[-1] != '9':
    d.append(a+str(int(a[-1])+1))

ans = a
print(ans)
#print(*ans,sep=' ')
