s = input()

sn = []
for i in range(len(s)-2):
  sn.append(int(s[i]+s[i+1]+s[i+2]))

answer = 1000
for check in sn:
  if answer >= abs(check - 753):
    answer = abs(check - 753)
  
print(answer)