N = int(input())
L = [0]*N
for X in range(1,101):
    for Y in range(1,101):
        for Z in range(1,101):
            Num = X*X+Y*Y+Z*Z+X*Y+X*Z+Y*Z
            if Num>N: break
            else: L[Num-1] += 1
print('\n'.join(str(X) for X in L))