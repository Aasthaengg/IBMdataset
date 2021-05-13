n=list(map(int, input().split()))+[1, 9, 7, 4]
if n.index(1)<4 and n.index(9)<4 and n.index(7)<4 and n.index(4)<4:
  print('YES')
else:
  print('NO')