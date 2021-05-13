s = input()

answer = 0
for i in s:
  if i == "+":
    answer = answer + 1
  if i == "-":
    answer = answer - 1  
print(answer)