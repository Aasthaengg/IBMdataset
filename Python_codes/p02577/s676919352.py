S = input()

cnt = 0
for ch in S:
  cnt += int(ch)
  
if cnt % 9 == 0:
  print("Yes")
else:
  print("No")
