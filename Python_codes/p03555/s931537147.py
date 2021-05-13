import sys
C1 = input()
C2 = input()
if C1[0] != C2[2]:
    print('NO')
    sys.exit()
else:
    if C1[1] != C2[1]:
        print('NO')
        sys.exit()
    else:
        if C1[2] != C2[0]:
            print('NO')
            sys.exit()
print('YES')