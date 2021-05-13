from collections import deque
H, W, M = map(int, input().split())
bomb = []
counth = [0 for k in range(H)]
countw = [0 for k in range(W)]
for k in range(M):
  h, w = map(int, input().split())
  h -= 1
  w -= 1
  bomb.append(h+ w*H)
  counth[h] += 1 
  countw[w] += 1

maxh = max(counth)
maxw = max(countw)
  
counth = deque(counth)
countw = deque(countw)

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            #return mid
            return True
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    #return None
    return False


index_h = deque([])
index_w = []
for k in range(H):
  h = counth.popleft()
  if h == maxh:
    index_h.append(k)

for k in range(W):
  w = countw.popleft()
  if w == maxw:
    index_w.append(k)

ans = maxh + maxw - 1
lenh = len(index_h)
lenw = len(index_w)


if lenh*lenw > M:
  ans += 1
else:
  bomb.sort()
  kouho = []
  for i in range(lenh):
    h = index_h.pop()
    for j in range(lenw):
      w = index_w[j]
      kouho.append(h+ H*w)
  for K in kouho:
    if binary_search(bomb, K):
      continue
    else:
      ans += 1
      break
    
print(ans)


