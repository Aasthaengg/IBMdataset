N = int(input())
B = list(map(int, input().split()))

A = []

for i in range(len(B)):
    if i == 0:
        A.append(B[i])
    else:
        if B[i-1] < B[i]:
            A.append(B[i-1])
        else:
            A.append(B[i])
A.append(B[i])

ANS = 0

for i in range(len(A)):
    ANS = ANS + A[i]
print(ANS)