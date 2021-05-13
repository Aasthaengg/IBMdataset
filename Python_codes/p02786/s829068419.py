H = int(input())
count = 1
i = 2
while H > 1:
  H //= 2
  count += i
  i *= 2
print(count)