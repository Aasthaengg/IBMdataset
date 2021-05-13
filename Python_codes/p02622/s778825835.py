s = input()
t = input()

count = 0
length = len(s)
for index in range(length):
  if not s[index] == t[index]:
    count += 1

print(count)