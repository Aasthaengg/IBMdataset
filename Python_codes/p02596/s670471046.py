s = int(input())
r=7
ret=-1
for a in range(1000000):
  if r % s == 0 :
    ret = a + 1
    break
  else:
    r=(r*10+7)%s
print(ret)