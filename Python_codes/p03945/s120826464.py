s = input()
ex = s[0]
count = 0
for c in s:
  if c!= ex:
    count +=1
    ex = c
print(count)