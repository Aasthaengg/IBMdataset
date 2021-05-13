s = list(input())
list1 = []
for i in range(len(s)-2):
  x = int(''.join(s[i:(i + 3)]))
  
  list1.append(abs(753 - x))
print(min(list1))