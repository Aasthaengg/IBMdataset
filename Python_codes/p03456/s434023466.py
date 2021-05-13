_list = input().split()
_int = int(_list[0]+_list[1])
_boolist = []
for i in range(_int):
  if i**2 == _int:
    _boolist.append("y")
  
if "y" in _boolist:
  print("Yes")
else:
  print("No")
    
#平方根を見つける
	#yesと出力
	#noの出力の場合
      #boolistの作成