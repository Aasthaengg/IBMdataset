S = input()
c, f = -1, -1
for i, s in enumerate(S):
    if s == 'C':
        c = i
        break
for i, s in enumerate(S[::-1]):
    if s == 'F':
        f = len(S)-i-1
        break
if c >= 0 and f >= 0 and c < f:
    print('Yes')
else:
    print('No')