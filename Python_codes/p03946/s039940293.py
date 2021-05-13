N, T = map(int, input().split())
A = list(map(int, input().split()))
C = 0
L = 10 ** 9 + 5
S = 0
for a in A:
    if a < L:
        L = a
    elif a > L:
        St = a - L
        if St == S:
            C += 1
        elif St > S:
            C = 1
            S = St
print(C)