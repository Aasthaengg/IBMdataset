n = int(input())
B = list(map(int, input().split()))
A = []
for b in B:
    A.insert(b-1, b)
if all(A[i] <= i+1 for i in range(n)):
    C = []
    for a in A:
        C.insert(a-1, a)
    if B == C:
        print(*A, sep='\n')
    else:
        print(-1)
else:
    print(-1)