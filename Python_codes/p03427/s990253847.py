Num = str(input())
L = len(Num)
if Num[1:] == '9'*(L-1):
  val = int(Num[0]) + 9*(L-1)
else:
  val = int(Num[0])-1 + 9*(L-1)
print(val)
