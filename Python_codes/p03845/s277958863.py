num_prob = int(input())
prob = input()
new = prob.split()
sum = 0

for j in new:
  sum += int(j)

  
num_drinks = int(input())
for i in range(num_drinks):
  line = input()
  new_line = line.split()
  if int(new_line[1]) != int(new[int(new_line[0])-1]):
    temp = sum - int(new[int(new_line[0])-1]) + int(new_line[1])
    print(temp)
  else:
    print(sum)
    
  
    
