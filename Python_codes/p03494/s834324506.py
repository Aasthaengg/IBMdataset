number = int(input())
target_list = input().split()

loopFlg = True
loopCnt = 0

while loopFlg == True:
  for i in range(number):
    if int(target_list[i])%2 == 1:
      loopFlg = False
    target_list[i] = str(int(target_list[i])//2)

  if loopFlg == True:
  	loopCnt += 1

print(loopCnt)