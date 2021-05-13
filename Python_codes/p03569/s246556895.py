from collections import deque
s = deque(list(input()))

ans = 0
while len(s) > 1:
  if s[0] != s[-1]:
    if s[0] == 'x':
      s.append('x')
    elif s[-1] == 'x':
      s.appendleft('x')
    else:
      print(-1)
      exit()
    ans += 1
  else:
    s.pop()
    s.popleft()
       
print(ans)