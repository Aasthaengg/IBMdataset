N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
c = 0
for i in range(N-1,-1,-1):
    if (A[i]+c) % B[i] == 0:
        continue
    if A[i]+c < B[i]:
        push = B[i] - (A[i]+c)
    elif A[i]+c > B[i]:
        push = B[i] - (A[i]+c) % B[i]
    c += push
print(c)