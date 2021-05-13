n, k = map(int, input().split())
lst = [int(i) for i in input().split()]

count = 0
min_price = 0
while count < k:
  #print(count)
  total = min_price
  for i in range(len(lst)):
    total += lst[i]
    #print(total)
    if i == 0:
      min_price = total
      min_index = i
    elif total < min_price:
      min_price = total
      min_index = i
    total -= lst[i]
  lst.pop(min_index)
  count += 1
print(min_price)