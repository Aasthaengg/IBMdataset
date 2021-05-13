import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

B = [0] * (max(A)+1)
C = []
for i in range(n):
    B[A[i]] += 1

C = A[:]
C.sort()
D = [0] * (10**6+5)

ans = 0
for i in range(len(C)):
    # print(C[i])
    if D[C[i]] == 0 and B[C[i]] == 1:
        ans += 1
    j = C[i]
    D[j] = 1
    if i==0 or C[i-1] != C[i]:
        while j < len(D):
            D[j] = 1
            j += C[i]
print(ans)