numLength = int(input())
numList = input().split()
count = 0
flag = True
while flag:
  for i in range(numLength):
    numList[i] = int(numList[i])
    if not numList[i] % 2 == 0:
      print(count)
      flag = False
      break
    numList[i] /= 2
  count += 1