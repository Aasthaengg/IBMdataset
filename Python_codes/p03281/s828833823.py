n = int(input())

answer = []
for i in range(1,n+1,2):
  check = 0
  for j in range(1,i+1):
    if (i) % j == 0:
      check += 1
      
  if check == 8:
    answer.append(i)
    
print(len(answer))