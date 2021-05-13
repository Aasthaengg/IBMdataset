import math
monsterNum, centerDamage, otherDamage = map(int, input().split())
monsterHitpoint = [0] * monsterNum
maxHitpoint = 0

def enough(times):
  result = True
  damageCount = 0
  hitpoint = [monsterHitpoint[i] - otherDamage * times for i in range(monsterNum)]
  for i in range(monsterNum):
    if hitpoint[i] > 0:
      damageCount += math.ceil(hitpoint[i] / (centerDamage - otherDamage))
    if damageCount > times:
      result = False
      break
  return result
  
for i in range(monsterNum):
  monsterHitpoint[i] = int(input())
  if maxHitpoint < monsterHitpoint[i]:
    maxHitpoint = monsterHitpoint[i]
#2分探索
low, high = 0, math.ceil(maxHitpoint / otherDamage)
while low <= high:
  minTimes = (low + high) // 2
  checkEnough = enough(minTimes)
  if checkEnough and not(enough(minTimes - 1)):
    break
  elif checkEnough:
    high = minTimes - 1
  elif not checkEnough and (enough(minTimes + 1)):
    minTimes += 1
    break
  elif not checkEnough:
    low = minTimes + 1
print(minTimes)