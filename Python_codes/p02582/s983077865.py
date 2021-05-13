s = input()
count = 0
result = 0
for c in s:
    if c == 'R':
        count+=1
        result = max(count, result)
    else:
        count = 0

print(result)