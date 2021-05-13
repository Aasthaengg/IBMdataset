upNum, firstNum, lastNum = map(int, input().split())
total = 0
digitNumSum = 0
for i in range(1, upNum + 1):
  digitNumSum = 0
  digitNumList = list(str(i))
  for j in range(len(digitNumList)):
    digitNumSum += int(digitNumList[j])
  if firstNum <= digitNumSum <= lastNum:
    total += i
print(total)