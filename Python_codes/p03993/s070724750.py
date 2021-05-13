N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
checked = [False] * N
ans = 0

for i in range(N):
    if not checked[i] and A[A[i]] == i:
        ans += 1
        checked[i] = True
        checked[A[i]] = True

print(ans)
