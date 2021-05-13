n, k = map(int, input().split())
r, s, p = map(int, input().split())
T = list(input())
ans = 0
commands = ['']*n
for i, t in enumerate(T):
  if t == 'r':
    command = 'p'
    point = p
  elif t == 's':
    command = 'r'
    point = r
  elif t == 'p':
    command = 's'
    point = s
  if (i - k >= 0) and (commands[i-k] == command):
    command = ''
    point = 0
  ans += point
  commands[i] = command
  
print(ans)