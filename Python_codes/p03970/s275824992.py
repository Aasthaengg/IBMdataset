s = input().rstrip()
t = 'CODEFESTIVAL2016'
count = 0
for i in range(len(s)):
  if s[i] != t[i]:
    count += 1
print(count)