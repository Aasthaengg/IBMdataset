#入力
lst = input().split()

a = lst[0]
b = lst[1]

#出力
if a == 'H': #Aは正直
   if b == 'H': #Tは正直:真
      print('H')
   elif b == 'D': #Tは嘘:真
      print('D')
elif a == 'D': #Aは嘘
   if b == 'H': #Tは正直:偽
      print('D')
   elif b == 'D': #Tは嘘:偽
      print('H')