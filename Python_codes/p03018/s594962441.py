s = raw_input()

count = 0
a = 0
i = 0
l = len(s)
while i < len(s):
    if s[i] == 'A':
        a += 1
        i += 1
        continue

    if s[i] == 'B' and i < l - 1 and s[i + 1] == 'C':
        count += a
        i += 2
    else:
        a = 0
        i += 1

print count
