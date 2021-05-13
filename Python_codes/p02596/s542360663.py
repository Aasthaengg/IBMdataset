k = int(input())

t = 7
flag = True
for i in range(k):
  if t % k == 0:
    print(i + 1)
    flag = False
    break
  else:
    t = (t * 10 + 7) % k
if flag:
  print('-1')