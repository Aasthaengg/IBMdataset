N = int(input())
A = [int(a) for a in input().split()]

ans = []
A.sort()
if A[0] >= 0:
    ans.append([A[0], A[1]])
    A[1] = A[0]-A[1]
    A.pop(0)
elif A[-1] <= 0:
    ans.append([A[-1], A[-2]])
    A[-2] = A[-1]-A[-2]
    A.pop(N-1)
for i in range(1, len(A)-1):
    if A[i] < 0:
        ans.append([A[-1], A[i]])
        A[-1] -= A[i]
    else:
        ans.append([A[0], A[i]])
        A[0] -= A[i]
if N > 2:
    ans.append([A[-1], A[0]])
print(A[-1]-A[0])
for a in ans:
    print(*a)