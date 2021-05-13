N, K = map(int, input().split())
list0, list1, list2 = [],[],[]
j = 1

if K % 2 == 1:
  i = K * 1
  while i <= N:
    list0.append(int(i))
    j += 1
    i = K * j
  ans = len(list0) ** 3
else:
  i = K / 2
  while i <= N:
    if j % 2 == 0:
      list1.append(int(i))
    if j % 2 == 1:
      list2.append(int(i))
    j += 1
    i = K * j / 2
  ans = len(list1) ** 3 + len(list2) ** 3
print(ans)