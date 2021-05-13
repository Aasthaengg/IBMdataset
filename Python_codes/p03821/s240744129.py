N = int(input())
A = [0]*N
B = [0]*N
for i in range (N):
    A[i],B[i] = map(int, input().split())
ctr = 0
for i in range (N-1, -1, -1):
    k = (A[i] + ctr) % B[i]
    if k != 0:
        ctr += B[i] - k
print(ctr)