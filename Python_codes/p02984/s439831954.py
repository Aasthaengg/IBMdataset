N = int(input())
A = list(map(int, input().split()))
A = [x * 2 for x in A]

x = 0
for i in range(N):
    x = A[i] - x
x = x // 2

ans = []
for i in range(N):
    ans.append(x)
    x = A[i] - x

print(*ans)
