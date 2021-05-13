S = input()
N = len(S)
f = True
if S[0] != 'A':
    f = False
if S[2:N-1].count('C') != 1:
    f = False
for s in S:
    if s != 'A' and s != 'C' and s.isupper():
        f = False
print('AC' if f else 'WA')