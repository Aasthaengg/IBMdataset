N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
prev = -1
ans = 0

for i,dish in enumerate(A):
    if prev+1 == dish:
        ans += C[prev-1]
    prev = A[i]
    ans += B[i-1]

print(ans)