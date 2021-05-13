N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        ans += A[0]
    else:
        ans += A[i//2]
print(ans)