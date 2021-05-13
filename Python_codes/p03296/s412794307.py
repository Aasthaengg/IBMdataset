N = int(input())
A = list(map(int, input().split()))

prev = A[0]
cnt = 1
ans = 0
for i in range(1, N):
    if A[i] == prev:
        cnt += 1
    else:
        ans += cnt // 2
        cnt = 1
        prev = A[i]
ans += cnt // 2
print(ans)