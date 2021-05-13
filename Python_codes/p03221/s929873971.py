n, m = map(int, input().split())
def zs(num):
    k = 6 - len(str(num))
    return '0' * k + str(num)
lst = []
for i in range(m):
  lst.append(tuple(map(int, input().split())))
slst = sorted(lst)
dic = {}
temp = 0
for i in range(m):
  if slst[i][0] == slst[i - 1][0]:
    temp += 1
  else:
    temp = 1
  dic[slst[i]] = zs(slst[i][0]) + zs(temp)
for i in lst:
  print(dic[i])