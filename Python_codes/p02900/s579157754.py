A, B = map(int, input().split())
def factorization(n):
  M = n
  k = 1
  faclist = [1]
  while(k**2 <= M):
    k += 1
    if M%k == 0:
      count = 0
      while M%k == 0:
        M //= k
        count += 1
      faclist.append(k)
  if M > 1:
    faclist.append(M)
  return faclist

a = factorization(A)
b = factorization(B)
from collections import deque

a = deque(a)
ans = 0
def binary_search(list, item):
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (low + high) //2
    guess = list[mid]
    if guess == item:
      return 1
    if guess > item:
      high = mid -1
    else:
      low = mid + 1
  return 0
while a:
  item = a.popleft()
  ans += binary_search(b, item)
print(ans)
  
