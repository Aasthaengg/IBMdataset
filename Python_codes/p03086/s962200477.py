s = input()
acgt = 'ACGT'
max_count = 0
i = 0
while i < len(s):
    count = 0
    if s[i] not in acgt:
        i += 1
        continue
    count += 1
    for j in range(i+1, len(s)):
        if s[j] not in acgt:
            break
        count += 1
    if count > max_count:
        max_count = count
    i += count + 1
print(max_count)
