s = input()
cs = 'CODEFESTIVAL2016'
count = 0
for i in range(len(s)):
    if s[i] != cs[i]:
        count += 1
print(count)