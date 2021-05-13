*S, = input()
ans = []

for s in S:
    if s == 'C':
        ans.append(s)
    if s == 'F':
        ans.append(s)

print('Yes' if 'CF' in ''.join(ans) else 'No')