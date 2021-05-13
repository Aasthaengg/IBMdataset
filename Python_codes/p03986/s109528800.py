s = input()

now_try = 0
idx = 0
while idx < len(s) - 1:

    if s[idx] == 'T':
        idx += 1
        continue

    if s[idx] == 'S':
        if s[idx + 1] == 'T':
            s = s[:idx] + s[idx + 2:]
            now_try += 1
            idx = idx - 1 if idx - 1 >= 0 else 0
        else:
            idx += 1

print(len(s))