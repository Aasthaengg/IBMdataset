N = int(input())
A = list(map(int, input().split()))

A.sort()
if A[0] == 0:
    ANS = 0
else:
    A.sort(reverse=True)
    ANS = 1
    for a in A:
        ANS = ANS * a
        if ANS > 10 ** 18:
            ANS = -1
            break

print(ANS)