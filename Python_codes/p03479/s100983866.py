import sys

X, Y = map(int, input().split())
tmp = X
count = 1

for i in range(100):
   tmp = tmp * 2
   if  tmp > Y:
       print(count)
       sys.exit()
   else:
       count += 1