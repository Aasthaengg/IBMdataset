s = input()
t = input()
count = 0
i = 0

while i < 3:
  if s[i] == t[i]:
    count += 1
  i += 1
print(count)