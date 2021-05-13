N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))
ans = B[A[0] - 1]
for i, a in enumerate(A[1:]):
    bef_a = A[i]
    ans += B[a - 1]
    if a - bef_a == 1:
        ans += C[bef_a - 1]
print(ans)