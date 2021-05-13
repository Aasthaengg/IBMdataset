N = input()
len_N = len(N)
count = 0

for i in range(len_N):
  count += int(N[i])
if count%9 == 0:
  print("Yes")
else:
  print("No")