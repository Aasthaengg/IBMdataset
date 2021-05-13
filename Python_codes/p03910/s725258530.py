n = int(input())
m = 0
d = 0
for i in range(10**4):
  if i*(i+1)//2 >= n:
    m = i
    d = i*(i+1)//2 - n
    break
for i in range(1,m+1):
  if i != d:
    print(i)
