N = int(input())
L = [111*i for i in range(10)]

flg = False
for i in range(9):
  if N // 10 == L[i] or N % 1000 == L[i]:
    flg = True
if flg:
  print("Yes")
else:
  print("No")
