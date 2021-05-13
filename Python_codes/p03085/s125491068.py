b = input()
res = ''

for s in b:
    if s == 'A':
        res += 'T'
    elif s == 'T':
        res += 'A'
    elif s == 'C':
        res += 'G'
    elif s == 'G':
        res += 'C'

print(res)
