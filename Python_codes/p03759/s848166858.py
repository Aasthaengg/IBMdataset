#入力
lst = input().split()

a = int(lst[0])
b = int(lst[1])
c = int(lst[2])

#出力
if b - a == c - b:
   print('YES')
else:
   print('NO')