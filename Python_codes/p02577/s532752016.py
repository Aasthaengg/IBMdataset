num = input()
le = len(num)
sum=0
for i in range(le):
  sum += int(num[i])
if sum%9==0:
  print("Yes")
else:
  print("No")