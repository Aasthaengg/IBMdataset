N = int(input())
A = [int(a) - 1 for a in input().split()]
ans = 0
for i in range(N):
    if A[A[i]] == i: ans += 1
print(ans // 2)