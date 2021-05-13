from collections import deque

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab = list(map(lambda x: [x[0], x[1], x[0]+x[1]], ab))
ab.sort(key=lambda x:x[2], reverse=True)
ab=deque(ab)
count = 0
ans=0
while len(ab)>0:
  a, b, dif = ab.popleft()
  if count%2==0:
    ans+=a
  else:
    ans-=b
  count+=1
print(ans)
