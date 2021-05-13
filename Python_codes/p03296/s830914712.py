N = int(input())
A = list(map(int, input().split()))
ans = 0
tmp = 1
for i in range(N-1):
    if A[i] == A[i+1]:
        tmp += 1
    else:
        ans += tmp // 2
        tmp = 1
ans += tmp // 2
print(ans)