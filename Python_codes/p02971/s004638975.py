N, *A = map(int, open(0).read().split())
B = sorted(A)
if B[-1] == B[-2]:
    for a in A:
        print(B[-1])
else:
    for a in A:
        if a != B[-1]:
            print(B[-1])
        else:
            print(B[-2])