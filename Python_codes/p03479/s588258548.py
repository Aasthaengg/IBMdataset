x,y = map(int,input().split())
maxx = y//x + 1
count = 0
for i in range(maxx):
  if x*(2**i) <= y:
    count += 1
  else:
    break
print(count)