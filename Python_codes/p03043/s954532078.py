n,k = map(int, input().split())

win = []

for i in range(1, n+1):
  if i >= k:
    win.append(1/n)
  else:
    t = True
    count = 0
    while t == True:
      if i < k:
        i = 2*i
        count += 1
      else:
        t = False
    win.append((((1/2)**count)*(min(n,k)/n))/min(n,k))

total = int(sum(win)*(10**12))/(10**12)
print(total)