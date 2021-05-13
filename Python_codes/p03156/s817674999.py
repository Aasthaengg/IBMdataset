N = int(input())
A, B = [int(_) for _ in input().split()]
P = [int(_) for _ in input().split()]

X = [0,0,0]
for p in P:
    if p <= A:
        X[0] += 1
    elif p <= B:
        X[1] += 1
    else:
        X[2] += 1

print(min(X))
