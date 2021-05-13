from collections import deque

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  d = deque()
  for i in range(n):
    if i % 2 == 0:
      d.append(a[i])
    else:
      d.appendleft(a[i])
  while len(d) > 0:
    if n % 2 == 0:
      print(d.popleft(), end=' ')
    else:
      print(d.pop(), end=' ')
  print('')
  return

if __name__ == "__main__":
  resolve()
