n = int(input())
a = sorted(list(map(int,input().split())))
double_cnt = 0
flag = 0
for i in range(n):
  if flag == a[i]:
    double_cnt += 1
  else:
    flag = a[i]
if double_cnt % 2 == 0:
  print(n-double_cnt)
else:
  print(n-double_cnt-1)