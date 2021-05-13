s = list(str(input()))

if s[-1] != 's':
    s.append('s')
else:
    s.append('es')

print(''.join(str(i) for i in s))
