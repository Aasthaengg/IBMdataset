from collections import deque

N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

A = deque(sorted(A,reverse=True))
B = deque([])
n = 0
for m in range(M):
    if A:
        if B:
            if (A[0] > B[0]):
                B.append(A.popleft()//2)
                continue
        else:
            B.append(A.popleft()//2)
            continue
    # print(m,n)
    n += 1
    b = B.popleft()
    B.append(b//2)

print(sum(A)+sum(B))