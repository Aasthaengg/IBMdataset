S = int(input())

A = [S]

while True:
    if S % 2 == 0:
        S //= 2
    else:
        S = 3*S + 1
    if not S in A:
        A.append(S)
    else:
        break

print(len(A)+1)