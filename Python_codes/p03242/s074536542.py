N = input()
N = list(N)
res = []
for n in N:
    if n is '1':
        res.append('9')
    else:
        res.append('1')

print(''.join(res))