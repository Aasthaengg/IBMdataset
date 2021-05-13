import sys
N = int(input())

input = sys.stdin.readline
lis = {}
for i in range(N):
  s = input().rstrip()
  if s in lis:
    lis[s] += 1
  else:
    lis[s] = 1
lis2 = sorted(lis.items(), key=lambda x:x[1], reverse=True)
x = next(iter(lis2))
keys = []
for i in lis2:
  if i[1] == x[1]:
    keys.append(i[0])
ans = sorted(keys)
for i in ans:
  print(i)