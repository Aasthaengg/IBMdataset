s = input().rstrip()
count = 0
for i in range(len(s)):
  if s[i] != 'CODEFESTIVAL2016'[i]:
    count += 1
print(count)
