#入力
lst = input().split()

#整数値化
for i in range(len(lst)):
   lst[i] = int(lst[i])

#ソート
lst.sort()

#出力
if lst[0] + lst[1] == lst[2]:
   print('Yes')
else:
   print('No')