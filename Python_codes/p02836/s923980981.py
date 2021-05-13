s = input()
s = list(s)
count = 0

for i in range(int(len(s)/2)):
  if s[i] == s[-(i+1)]:
    continue
  else:
    count += 1
    
print(count)