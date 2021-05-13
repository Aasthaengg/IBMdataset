# D - Non-decreasing

N = int(input())
A = list(map(int, input().split()))

A_min = min(A)
A_max = max(A)

ans = []

if abs(A_max) >= abs(A_min):
    A_max_idx = A.index(A_max)
    for i in range(1,N+1):
        ans.append([A_max_idx + 1, i])
    for i in range(1,N):
        ans.append([i, i+1])
else:
    A_min_idx = A.index(A_min)
    for i in range(1,N+1):
        ans.append([A_min_idx + 1, i])
    for i in reversed(range(2,N+1)):
        ans.append([i, i-1])
        
print(len(ans))
for x in ans:
    print(*x)
#     A[x[1]-1] += A[x[0]-1]
#     print(A)