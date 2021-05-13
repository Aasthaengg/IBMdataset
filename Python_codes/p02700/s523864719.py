A, B, C, D = map(int, input().split())
while A > 0:
    C -= B
    if C <= 0:
        print('Yes')
        exit()
    A -= D
print('No')