N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = 0
S = 0
T = []
if sum(A) < sum(B):
    K = -1
else:
    for i in range(N):
        if A[i] < B[i]:
            K += 1
            S = S + B[i] - A[i]
        elif A[i] > B[i]:
            T.append(A[i] - B[i])
        else:
            continue
T.sort()
L = 0
while S > L:
    L += T.pop()
    K += 1
print(K)
