N = int(input())

A = list(map(int, input().split()))

tmp = 0
for i in range(N):
    tmp = A[i] * 2 - tmp

tmp //= 2
ans = []
for i in range(N):
    ans.append(tmp)
    tmp = A[i] * 2 - tmp

print(*ans)