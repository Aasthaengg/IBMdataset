input_str = input().split()
k = int(input_str[0])
s = int(input_str[1])

count = 0
for x in range(k+1):
  for y in range(k+1):
    if x+y <= s:
      z = s-(x+y)
      if z <= k:
        count += 1
print(count)