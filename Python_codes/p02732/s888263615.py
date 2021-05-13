n = int(input())
lst = list(map(int, input().split()))
dic = {}
allsum = 0
for i in range(n):
  dic.setdefault(lst[i], 0)
  dic[lst[i]] += 1
  if dic[lst[i]] >= 2:
    allsum += (dic[lst[i]] - 1)
for i in range(n):
  a = dic[lst[i]]
  temp = allsum - ((a * (a - 1)) // 2)
  if a - 1 >= 2:
    b = a - 1
    temp += ((b * (b - 1)) // 2)
  print(temp)