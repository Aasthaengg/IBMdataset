line = list(input())
answer = "Good"
for i in range(3):
  if line[i] == line[i+1]:
    answer = "Bad"
    break
    
print(answer)