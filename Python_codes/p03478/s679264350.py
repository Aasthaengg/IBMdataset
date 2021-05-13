input_line = input()
x, y, z = map(str, input_line.split())

resultNum = 0

for i in range(int(x)+1):
  loopCnt = len(str(i))
  addNum = 0
  for j in range(loopCnt):
    addNum += int(str(i)[j])
  if int(y) <= addNum <= int(z):
    resultNum += i

print(resultNum)