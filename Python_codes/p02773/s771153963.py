from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for i in range(n):
  dic[input()] += 1
max_s = max(dic.values())
for k, v in sorted(dic.items()):
  if v == max_s:
    print(k)