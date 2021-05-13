N = int(input())
A = list(map(int,input().split()))
MAX = max(A)
MIN = min(A)

print(2 * N - 1)

if MAX >= -1 * MIN:
    j = A.index(MAX)
    for i in range(N):
        print(*[j+1, i+1])
    for i in range(N-1):
        print(*[i+1, i+2])
else:
    j = A.index(MIN)
    for i in range(N):
        print(*[j+1, i+1])
    for i in range(N-1,0,-1):
        print(*[i+1, i])