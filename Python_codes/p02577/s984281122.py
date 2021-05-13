N = input()
s = len(N)
sum = 0

for i in range(s):
  sum += int(N[i])
  
if sum % 9 == 0:
  print("Yes")
  
else:
  print("No")