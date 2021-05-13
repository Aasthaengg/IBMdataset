init1, init2 = map(int, input().split(" "))

resultFlag = (init1 * init2)%2

if resultFlag == 0:
  print('Even')
else:
  print('Odd')