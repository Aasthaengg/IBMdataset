data = int(input())
array = [int(i) for i in input().split()]
div2 = 0
div4 = 0
for i in array:
  if i%4==0:
    div4 += 1
  elif i%2==0:
    div2 += 1
if data-max(div2-1,0) <= div4*2+1:
  print('Yes')
else:
  print('No')