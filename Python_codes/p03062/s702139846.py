N = int(input())
A = list(map(int,input().split()))
B = [abs(i) for i in A]
ans1 = sum(B) - 2 * min(B)
for i in range(N - 1):
    if A[i] < 0:
        A[i] = -A[i]
        A[i + 1] *= -1
ans2 = sum(A)
ans = max(ans1, ans2)
print(ans)