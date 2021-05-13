s = int(input())
T = set()
T.add(s)
for i in range(1000001):
  if s%2:
    s = s*3 + 1
  else:
    s = s // 2
  l = len(T)
  T.add(s)
  if l == len(T):
    print(i+2)
    exit()