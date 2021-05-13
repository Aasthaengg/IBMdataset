# 回答を見て作成：一致検索はsort＋一致で時間がかかる？
n = int(input())
a = [int(x.strip()) for x in input().split()]
b = []
ans = str('')
for i in enumerate(a):
  b.append(i)
b.sort(key=lambda x:x[1])
for i in b:
  print(i[0]+1)