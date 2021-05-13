import sys
input = sys.stdin.readline

N = int(input())
tak, aok = 1, 1
for _ in range(N):
    T, A = map(int, input().split())
    if T == A:
        tak = aok = max(tak, aok)
    else:
        f = (tak + T - 1) // T
        t = f * T
        a = f * A
        if a >= aok:
            tak = t
            aok = a
        else:
            f = (aok + A - 1) // A
            tak = f * T
            aok = f * A
print(tak + aok)
