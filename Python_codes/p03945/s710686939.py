s = input()
count = 0
for i in range(len(s)):
  if(i==0):
    now = s[i]
  else:
    if(s[i] != now):
      count += 1
  now = s[i]
print(count)