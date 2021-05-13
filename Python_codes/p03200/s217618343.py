s = input()

total = 0
count = 0
for i in range(len(s)):
  if s[i] == 'W' :
    total += i - count
    count += 1

print(total)
