S=input()
chars = []
for c in S:
    chars.append(c)

ans = len(S) == len(set(chars))

if ans:
    print('yes')
else:
    print('no')