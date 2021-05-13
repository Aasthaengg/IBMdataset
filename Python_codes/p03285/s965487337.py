n = int(input())

answer = False
for num_4 in range(n//4+1):
  if (n-num_4*4)%7 == 0:
    answer = True 
    break

if answer :
  print("Yes")
else :
  print("No")