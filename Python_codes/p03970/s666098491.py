s = input()
TITLE = 'CODEFESTIVAL2016'
count = 0

for c in range(len(s)):
    if s[c] != TITLE[c]:
        count += 1

print(count)