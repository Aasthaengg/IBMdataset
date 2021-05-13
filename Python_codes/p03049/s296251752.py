N = int(input())

S = []
D = {'ab': 0, 'a': 0, 'b': 0}

res = 0
for _ in range(N):
    s = input()
    res += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        D['ab'] += 1
    elif s[0] == 'B':
        D['b'] += 1
    elif s[-1] == 'A':
        D['a'] += 1

if D['ab'] > 0:
    res += D['ab'] - 1
    res += int(D['a'] > 0) + int(D['b'] > 0)
    res += max(0, min(D['a'] - 1, D['b'] - 1))
else:
    res += min(D['a'], D['b'])

print(res)
