s = input()
even, odd = [], []
for i in range(len(s)):
    if i%2:
        odd.append(s[i])
    else:
        even.append(s[i])
e = list(set(odd))
o = list(set(even))
if('L' in o or 'R' in e):
    print('No')
else:
    print('Yes')