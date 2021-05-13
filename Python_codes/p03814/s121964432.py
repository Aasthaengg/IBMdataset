s = input()

for i in range(0, len(s)):
    if s[i] == 'A':
        start_idx = i
        break
for i in reversed(range(0, len(s))):
    if s[i] == 'Z':
        end_idx = i
        break
print(end_idx - start_idx + 1)
