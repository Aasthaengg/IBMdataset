n = int(input())
l = list(map(int, input().split()))
tot = sum(l)
flag = True
for l_i in l:
  if 2 * l_i >= tot:
    flag = False
    break
if flag:
  print('Yes')
else:
  print('No')