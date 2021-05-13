n = int(input().rstrip())
cnt = 0
flg = False
d_list = [[0, 0] for i in range(n)]
for i in range(n):
  d_list[i] = list(map(int, input().rstrip().split(" ")))
for ds in d_list:
  if ds[0] == ds[1]:
    cnt += 1
  else:
    cnt = 0
  if cnt >= 3:
    flg = True
    break
if flg:
  print("Yes")
else:
  print("No")