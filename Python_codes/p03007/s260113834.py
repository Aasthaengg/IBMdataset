from collections import deque
plusQ = deque([]) 
minsQ = deque([])
 
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
 
for itr, val in enumerate(A):
  if itr == 0:
    plusQ.append(val)
  elif itr != len(A) - 1 and val > 0:
    plusQ.append(val)
  else:
    minsQ.append(val)
    
p1 = plusQ.popleft()
 
ans = deque([])
while len(minsQ) > 0:
  if len(plusQ) > 0:
    p, m = plusQ.popleft(), minsQ.popleft()
    ans.append([m, p])
    minsQ.append(m - p)    
  else:
    m = minsQ.popleft()
    ans.append([p1, m])
    p1 = p1 - m

print(p1)
while len(ans) > 0:
  hoge = ans.popleft()
  print(hoge[0],hoge[1])