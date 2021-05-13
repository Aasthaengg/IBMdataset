number, color = map(int, input().split())
answer = 1
for i in range(number):
  if(i ==0):
    answer = answer*color
  else:
    answer = answer*(color - 1)
    
print(answer)