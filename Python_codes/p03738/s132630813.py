A = input()
B = input()

import sys
if len(A)>len(B):
    print('GREATER')
    sys.exit()
elif len(A)<len(B):
    print('LESS')
    sys.exit()
else:
    for a,b in zip(A,B):
        if int(a)>int(b):
            print('GREATER')
            sys.exit()
        elif int(a)<int(b):
            print('LESS')
            sys.exit()
print('EQUAL')