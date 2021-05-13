
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)
for i, a in enumerate(A):
    if i >= len(A) - 1:
        break
    if a + 1 == A[i+1]:
        ans = ans + C[a-1]
print(ans)