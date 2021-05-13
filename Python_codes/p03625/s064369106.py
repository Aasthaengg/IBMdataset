import collections
n = int(input())
a = [int(i) for i in input().split()]
dic = collections.defaultdict(int)

for i in range(n):
  dic[a[i]] += 1
ans = 0
ls = list(dic.keys())
ls.sort()
ans_ls = []

for i in range(len(ls)-1,-1,-1):
  if dic[ls[i]] >= 2:
    ans_ls.append(ls[i])
  if dic[ls[i]] >= 4:
    ans_ls.append(ls[i])
if len(ans_ls) < 2:
  print(0)
else:
  print(ans_ls[0] * ans_ls[1])