A, B = map(int, input().split(' '))

diff = abs(A - B)
total = A + B
rest = 16 - total

if rest >= diff:
    print('Yay!')
else:    
    print(':(')
