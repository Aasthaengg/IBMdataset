N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
if len([a for a in A if a * 4 * M >= S]) >= M:
    print('Yes')
else:
    print('No')