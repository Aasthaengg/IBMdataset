A, B, C, D = map(int, input().split())

sw = 0
while sw == 0:
    if C > 0:
        C = C - B
    else:
        sw = 1
        break
    if A > 0:
        A = A - D
    else:
        sw = 2
        break
if sw == 1:
    print('Yes')
else:
    print('No')