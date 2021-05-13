n = int(input())
a = list(map(int,input().split()))
odd = 0
even4 = 0
for num in a:
  if num%2 == 1:
    odd += 1
  elif num%4 == 0:
    even4 += 1
if odd + even4 == n and even4 >= odd-1:
  print('Yes')
elif even4 >= odd:
  print('Yes')
else:
  print('No')