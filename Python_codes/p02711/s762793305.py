n = int(input())
num = []
while n>0:
  num.append(n%10)
  n //= 10

ans = 0
for i in num:
  if i == 7:
    ans+=1
    break
  else:
    ans = 0
    
if ans >= 1:
  print("Yes")
elif ans==0:
  print("No")