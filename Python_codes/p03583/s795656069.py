N = int(input())
# 4/n = 1/h+1/n+1/w
for h in range(1,3501):
  for n in range(h,3501):
    w1 = N*h*n
    w2 = 4*h*n-N*n-N*h
    if w2 == 0:
      continue
    if w1%w2 == 0:
      w = w1//w2
      if w > 0:
        print(h,n,w)
        exit()