from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
if K >= sum(A):
  print(0)
  exit()
A.sort(reverse=True)
F.sort()
lot = []
for k in range(N):
  lot.append((A[k]*F[k], k))
lot.sort(key =  lambda x:x[0],reverse=True)
high = lot[0][0]
#print('A:', A)
#print('F:', F)
#rint(lot)
def binary_search(high):
  low = 0
  mid = (low + high) //2
  while low < high:
    final = False
    mid = (low + high) //2
    #print(low, high, mid)
    if low == high-1:
      final = True
    #print(low, high, mid)
    res = K
    flag = True
    for k in range(N):
      if res < 0:
        break
      else:
        if lot[k][0] <= mid:
          break
        else:
          res -= ceil((lot[k][0]-mid)/F[lot[k][1]])
          continue
    if res < 0:
      flag = False
    #print(flag)
    if flag:
      high = mid
    else:
      if final:
        mid += 1
      low = mid
    #print(low, high, mid)
  #return None
  return mid

print(binary_search(high))