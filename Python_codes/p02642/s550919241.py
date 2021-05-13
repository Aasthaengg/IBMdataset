from collections import Counter, defaultdict

n = int(input())
a = list(map(int, input().split()))
dic = Counter(a)
memo1 = set()
memo2 = set()

MAX = 10 ** 6 + 1
for i in a:
  if i in memo1:
    continue
  if i in dic:
    if dic[i] > 1:
      memo2.add(i)
  for j in range(i*2, MAX, i):
    if j in dic:
      memo2.add(j)
  memo1.add(i)
ans = len(memo1) - len(memo2)
print(ans)