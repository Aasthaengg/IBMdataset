N = int(input())
A = list(map(int, input().split()))
t = A[0]
ans = 0
for i in range(1, N):
    if A[i] > t:
        t = A[i]
    elif A[i] == t:
        pass
    else:
        ans += t - A[i]
print(ans)