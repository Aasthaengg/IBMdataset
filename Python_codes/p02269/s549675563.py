a = {}

n = int(input())

for i in range(n):
  cmd, val = input().split()
  if cmd == 'insert':
    a[val] = val
  elif cmd == 'find':
    print('yes' if val in a else 'no')
