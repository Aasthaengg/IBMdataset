from collections import deque
K = int(input())
d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

if K <= 9:
  print(K)
else:
  for i in range(K):
    num = d[0]
    d.popleft()
    plus = int(10*num + num%10)
    if num % 10 != 0:
      d.append(plus-1)
    d.append(plus)
    if (i<K) and (num%10!=9):
      d.append(plus+1)
  print(num)