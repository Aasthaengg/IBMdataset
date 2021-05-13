A, B, C, D = map(int, input().split())

while 1:
    C = C - B
    if C <= 0:
        print('Yes')
        exit(0)
    A = A - D
    if A <= 0:
        print('No')
        exit(0)