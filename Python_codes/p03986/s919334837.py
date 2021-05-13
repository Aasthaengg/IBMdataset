string = input()

length = len(string)
sindex = 0
for i in range(0, length):
  if string[i] == "S": 
    sindex = i
    break
    
s_count = 0

for i in range(sindex, len(string)):
  if string[i] == "S": s_count += 1
  if string[i] == "T" and s_count > 0:
    s_count -= 1
    length -= 2
    
print(length)