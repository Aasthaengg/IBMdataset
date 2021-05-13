s = list(input())
count = 0
list1 = []
for x in s:
  if x == 'A' or x == 'G' or x == 'T' or x == 'C':
    count = count + 1
  list1.append(count)
  if x != 'A' and x != 'G' and x != 'T' and x != 'C':
    count = 0
    

print(max(list1))