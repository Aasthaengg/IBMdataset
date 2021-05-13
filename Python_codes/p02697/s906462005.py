N, M = map(int, input().split())
 
if M % 2 == 0:
  l = 1
  for i in range(M//2):
    L = []
    L.append(l)
    L.append(2*(M//2-i)+l)
    print(*L)
    l += 1
  l = 2*(M//2)+2
  for i in range(M//2):
    L = []
    L.append(l)
    L.append(2*(M//2-i)+l-1)
    print(*L)
    l += 1
  
  
elif M % 2 == 1:
  l = 1
  for i in range(M//2):
    L = []
    L.append(l)
    L.append(2*(M//2-i)+l)
    print(*L)
    l += 1
  l = 2*(M//2)+2
  for i in range(M//2+1):
    L = []
    L.append(l)
    L.append(2*(M//2+1-i)+l-1)
    print(*L)
    l += 1