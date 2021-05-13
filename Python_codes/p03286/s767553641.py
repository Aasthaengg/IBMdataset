n = int(input())
l = []
c = 1
while n != 0:
    if n % 2**c !=0:
        n -= (-2)**(c-1)
        l.append('1')
    
    else:
        l.append('0')
    
    c += 1

if len(l) == 0:
    print('0')

else:
    print(''.join(reversed(l)))