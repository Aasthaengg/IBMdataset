n = int(input())
k = int(input())
tmp = 1
i = 0
while True:
  a = 0
  b = 0
  if i == n:
    break
  else:
    a = tmp * 2
    b = tmp + k
    tmp = min(a,b)
    #print(tmp)
    i += 1
print(tmp)