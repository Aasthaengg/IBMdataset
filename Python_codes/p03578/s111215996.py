n = int(input())
d = list(map(int, input().split()))
p = {}
for i in d:
  if i not in p:
    p[i] = 1
  else:
    p[i] += 1
m = int(input())
t = list(map(int, input().split()))
for i in t:
  if i not in p or p[i] == 0:
    print('NO')
    break
  else:
    p[i] -= 1
else:
  print('YES')
