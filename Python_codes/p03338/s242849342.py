n = int(input())
s = input()

answer = 0
for index in range(1,len(s)-1):
  x = list(set(s[:index]))
  y = list(set(s[index:]))
  count = 0
  if len(x) > len(y):
    for check in x:
      if check in y:
        count += 1
  else:
    for check in y:
      if check in x:
        count += 1
  if count > answer:
    answer = count
  
print(answer)