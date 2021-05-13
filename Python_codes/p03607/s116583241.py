from collections import defaultdict

N = int(input())

dic = defaultdict(bool)
for _ in range(N):
  a = int(input())
  dic[a] = not dic[a]

print(sum(dic.values()))