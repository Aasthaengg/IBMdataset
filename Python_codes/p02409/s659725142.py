def Input(b, f, rn, h):
    A[b][f][rn] += h

def Output():
    for b in range(4):
        for f in range(4):
            for rn in range(10):
                if f < 3:
                    print(' ' + str(A[b][f][rn]), end = '')
                if f == 3 and b != 3:
                    print('##', end = '')
            if b == 3 and f == 3:
                break
            print()

n = int(input())

A = [[[0 for rn in range(10)] for f in range(3)] for b in range(4)]

for idx in range(n):
    R = input().split()
    B = int(R[0]) - 1
    F = int(R[1]) - 1
    RN = int(R[2]) - 1
    H = int(R[3])
    Input(B, F, RN, H)
Output()