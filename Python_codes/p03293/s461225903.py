from collections import deque
s = input()
t = input()

u = deque(s)
ok = False
for i in range(len(s)):
  u.rotate(1)
  if ''.join(u) == t:
    ok = True
    
print('Yes' if ok else 'No')