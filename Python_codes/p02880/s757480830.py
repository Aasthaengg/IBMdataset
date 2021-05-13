n = int(input())
numlist = [1,2,3,4,5,6,7,8,9]
flag = False

for i in numlist:
  ans1 = n / i
  for j in numlist:
    ans2 = ans1 / j
    if ans2 == 1:
      flag = True
      
if flag:
  print('Yes')
else:
  print('No')