s = input()
query ='CODEFESTIVAL2016'
ct = 0
for i in range(len(s)):
  if s[i] != query[i]:
    ct += 1
print(ct)