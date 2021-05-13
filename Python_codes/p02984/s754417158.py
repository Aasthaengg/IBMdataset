N = int(input())
A = list(map(int, input().split()))

total = 0
ans = []
re = 1

for i in range(N):
    total += re*A[i]
    re *= -1
ans.append(total)

for j in range(N-1):
    ans.append(2*A[j]-ans[j])

print(" ".join(map(str, ans)))