from collections import defaultdict
dic = defaultdict(int)
n,m = map(int, input().split())
for _ in range(m):
  a, b = map(int, input().split())
  dic[a] += 1
  dic[b] += 1
flag = True
for k,v in dic.items():
  if v % 2 == 1:
    flag = False
    break
if flag:
  print("YES")
else:
  print("NO")
