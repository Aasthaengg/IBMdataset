h = int(input())
w = int(input())
n = int(input())
count1 = 0
count2 = 0

if h > w:
  while w > 0:
    count1 += h
    if count1 >= n:
      count2 += 1
      break
    else:
      count2 += 1
      w -= 1
else:
  while h > 0:
    count1 += w
    if count1 >= n:
      count2 += 1
      break
    else:
      count2 += 1
      h -= 1

print(count2)