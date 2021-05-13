N = int(input())
A = [int(x) for x in input().split()]
maxA, minA = max(A), min(A)
if maxA >= abs(minA):
    OP = [(A.index(maxA)+1, i+1) for i in range(N)] + [(i, i+1) for i in range(1,N)]
else:
    OP = [(A.index(minA)+1, i+1) for i in range(N)] + [(i+1, i) for i in reversed(range(1,N))]
print(len(OP))
for op in OP: print(*op)       