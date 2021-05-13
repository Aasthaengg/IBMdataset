s = input()

c_idx = len(s)
f_idx = -1
for i in range(len(s)):
    if s[i] == 'C':
        c_idx = min(c_idx, i)
    if s[i] == 'F':
        f_idx = max(f_idx, i)
print('Yes' if c_idx < f_idx else 'No')
