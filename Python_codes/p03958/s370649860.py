import sys
R1 = input().split()
R2 = input().split()
K = int(R1[0])
T = int(R1[1])
answer = int(0)
A = []
for i in range (0, T):
    A.append(int(R2[i]))
A.sort()
A.reverse()
if T == 1:
    print(A[0] - 1)
    sys.exit()
if T == 2:
    print(A[0] - A[1] - 1)
    sys.exit()
for i in range (0, K):
    C = A[0]
    if C - 1 > A[1]:
        if A[1] == 0:
            answer += 1
        if A[1] != 0:
            K -= 1
            D = int(A[1])
            A.remove(D)
            F = int(1)
            left = int(0)
            right = int(T - 2)
            while (left <= right):
                mid = int(left + (right - left) / 2)
                if A[mid] >= D - 1:
                    left = mid + 1
                    F = max(F, mid + 1)
                else:
                    right = mid - 1
            A.insert(F, D - 1)
        A[0] -= 1
    if C - 1 == A[1]:
        A[0] -= 1
    if C == A[1]:
        F = int(0)
        left = int(0)
        right = int(T - 1)
        while (left <= right):
            mid = int(left + (right - left) / 2)
            if A[mid] == C:
                left = mid + 1
                F = max(F, mid + 1)
            else:
                right = mid - 1
        A.insert(F, C - 1)
        A.remove(C)
print(answer)