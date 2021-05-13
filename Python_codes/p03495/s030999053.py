n,k = map(int, input().split())
li = list(map(int, input().split()))

dic = {}
for i in li:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

val = sorted(dic.values())

ans = 0
if k > len(val):
  print(ans)
else:
  a = len(val) - k
  ans = sum(val[:a])
  print(ans)