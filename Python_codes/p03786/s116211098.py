N = int(input())
A = list(map(int, input().split()))
A.sort()
sm = 0
p = -1
# print(A)
for i in range(N-1):
    sm += A[i]
    if 2*sm < A[i+1]:
        p = i
    # print(sm,2*A[i+1])
# print(p)
print(N-p-1)
