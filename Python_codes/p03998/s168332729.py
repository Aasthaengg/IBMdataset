S = dict()
S['a'] = list(input())[::-1]
S['b'] = list(input())[::-1]
S['c'] = list(input())[::-1]

p = 'a'
while S[p]:
    p = S[p].pop()
print(p.upper())