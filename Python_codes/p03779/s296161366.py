x = int(input())

y = 0
i = 1
cnt = 0
while y < x:
   y += i
   i += 1
   cnt += 1
   if y >= x:
      break
print(cnt)
