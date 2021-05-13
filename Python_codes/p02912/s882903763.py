from collections import deque
n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

A = deque(sorted(a,reverse=True))
B = deque([])

for _ in range(m):
    #if _ % (m//10) == 0: print(A, B)
    if A:
        if B:
            if (A[0] > B[0]):
                B.append(A.popleft()//2)
                continue
        else:
            B.append(A.popleft()//2)
            continue
    b = B.popleft()
    B.append(b//2)

print(sum(A)+sum(B))
