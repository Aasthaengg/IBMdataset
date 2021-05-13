import math
N, K = list(map(int, input().split()))
p = list(map(int, input().split()))

def quickSort(arr):
  if len(set(arr)) == 1:
    return arr
  res = []
  pivot = arr[math.floor(len(arr)/2)]
  left = []
  right = []
  center = []
  for i in arr:
    if i < pivot:
      left.append(i)
    elif i > pivot:
      right.append(i)
    else:
      center.append(i)
  if len(left) != 0:
    res = quickSort(left)
  res.extend(center)
  if len(right) != 0:
    res.extend(quickSort(right))
  return res

p = quickSort(p)
print(sum(p[:K]))