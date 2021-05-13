s=input()
List=["eraser","erase","dreamer","dream"]
for item in List:
  s = s.replace(item,'')
if len(s)==0:
  print('YES')
else:
  print('NO')