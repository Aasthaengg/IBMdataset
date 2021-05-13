n = int(input())
a = list(map(int, input().split()))

b1 = 0
b2 = 0
b4 = 0
for i in range(n):
   if a[i] % 4 == 0:
      b4 += 1
   elif a[i] % 2 == 0:
      b2 += 1
   else:
      b1 += 1
if b2 == 0:
   b4 += 1
if b1 <= b4:
   print('Yes')
else:
   print('No')
