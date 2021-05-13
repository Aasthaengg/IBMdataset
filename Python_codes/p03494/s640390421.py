N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    cnt = 0
    while A[i] % 2 == 0:
        A[i] = A[i] / 2
        cnt = cnt + 1
    ans.append(cnt)
print(min(ans))