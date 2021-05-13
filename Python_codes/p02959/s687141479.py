n = int(input())
A = list(map(int, input().split()))
B = tuple(map(int, input().split()))

ans = 0
for i, b in enumerate(B):
    rem = max(0, b-A[i])
    ans += min(A[i], b)
    ans += min(A[i+1], rem)
    A[i+1] = max(0, A[i+1]-rem)

print(ans)
