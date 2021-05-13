A,B=map(int,input().split())
flag = True
res = 0
for i in range(2000):
  n8 = int(i * 0.08)
  n10 = int(i* 0.1)
  if n8 == A and n10 == B:
    flag = False
    res = i
    break
  elif n10 == A and n8 == B:
    flag=False
    res = i
    break
  else:
    pass
if flag:
  print(-1)
else:
  print(res)