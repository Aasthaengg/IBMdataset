from collections import deque
S = deque(input())
ans = list()
while S:
  tmp = S.popleft()
  if not ans:
    ans.append(tmp)
    continue
  if ans[-1] == tmp:
    if S:
      tmp += S.popleft()
    else:
      break

  ans.append(tmp)
    
print(len(ans))