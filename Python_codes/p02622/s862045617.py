s = input().rstrip()
t = input().rstrip()
count = 0
for i, c in enumerate(s):
  if c != t[i]:
    count += 1
print(count)