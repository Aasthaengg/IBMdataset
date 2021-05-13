a, b = map(int, input().split())

count = 0
for i in range(1, a):
   count += 1
if (b >= a):
   print(count + 1)
else:
   print(count)
