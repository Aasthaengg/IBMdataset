n = int(input())
quo = int(n/1.08)
temp = 0
while temp<= n:
  temp = int(quo*1.08)
  if temp == n:
    print(quo)
    break
  quo = quo+1
if temp > n:
  print(':(')