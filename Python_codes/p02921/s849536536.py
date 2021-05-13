s = input()
t = input()
count = 0
if s[0:1] == t[0:1]:
  count += 1
if s[1:2] == t[1:2]:
  count += 1
if s[2:3] == t[2:3]:
  count += 1
print(count)