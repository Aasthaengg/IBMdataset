A, B, X = map(int, input().split())

def calc(N, X):
    if N < 0:
        return 0
    return N // X + 1

P = calc(A-1, X)
Q = calc(B, X)

print(Q-P)