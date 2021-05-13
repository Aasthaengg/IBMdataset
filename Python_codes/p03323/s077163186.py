A, B = map(int, input().split())
cakes = 'E'*A + 'S'*B + '0' *(16-A-B)

while 'ES' in cakes:
    cakes = cakes.replace('ES', '')
while 'E0' in cakes:
    cakes = cakes.replace('E0', '')
while 'S0' in cakes:
    cakes = cakes.replace('S0', '')

if 'EE' in cakes or 'SS' in cakes:
    print(':(')
else: print('Yay!')
