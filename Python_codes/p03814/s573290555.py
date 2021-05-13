s = list(input())
count = 0
for i in s:
    if (i == 'A'):
        break
    count += 1
for i in s[::-1]:
    if (i == 'Z'):
        break
    count += 1
print(len(s) - count)