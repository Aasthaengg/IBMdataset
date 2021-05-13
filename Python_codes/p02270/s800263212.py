from collections import deque

nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
w = []
for i in range(0, n):
  w.append(int(input()))

# 1台あたりの積載量がvのとき、荷物の配列aを積めるか返す
def allocatable(a, v):
  b = deque(a)
  currentCar = 0
  wSum = 0
  while currentCar < k:
    weight = b.popleft()
    if wSum + weight <= v:
      wSum += weight
    else:
      # 積み切れなければbに戻して次の車へ
      b.appendleft(weight)
      currentCar += 1
      wSum = 0
    # bに要素が残っていなければ積み切った => True
    if not b:
      return True
  # 最後の車まで来て残っていればFalse
  return not b

# 最小の積載量Pを求める
def search(a):
  l = 0
  r = 1000000000
  while l + 1 < r:
    i = int((l + r) / 2)
    if allocatable(a, i):
      r = i
    else:
      l = i
  return r

print(search(w))
