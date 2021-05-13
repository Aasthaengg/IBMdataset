import math
N = int(input()) #総数
s = input()      #文字列
count = 0
for i in s:
  if i == "R":
    count = count + 1
if count > N//2:
  print("Yes")
else:
  print("No")