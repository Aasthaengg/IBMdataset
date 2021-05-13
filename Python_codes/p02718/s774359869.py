N, M = map(int, input().split())
A = list(map(int, input().split()))

cn = 0
SUM = 0

for i in range(len(A)):
    SUM = SUM + A[i]
    
for i in range(len(A)):
    if A[i] >= (SUM / 4 / M):
        cn = cn + 1
    else:
        continue

if cn >= M:
    print('Yes')
else:
    print('No')