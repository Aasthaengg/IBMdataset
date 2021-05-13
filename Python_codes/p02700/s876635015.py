# 164_b
A, B, C, D = map(int, input().split())
if (1 <= A and A <= 100) and (1 <= B and B <= 100) and (1 <= C and C <= 100) and (1 <= D and D <= 100):

    while True:
        C = C - B
        A = A - D

        if A <= 0 or C <= 0:
            break
    if C <= 0:
        print('Yes')
    elif A <= 0:
        print('No')