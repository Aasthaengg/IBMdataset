X, N = list(map(int, input().split()))

p = list(map(int, input().split()))

count_up= 0
count_down = 0
while True:
  if not X + count_up in p:
    break
  count_up += 1
    
while True:
  if not X - count_down in p:
    break
  count_down += 1

if count_up < count_down:
  print(X+count_up)
else:
  print(X-count_down)