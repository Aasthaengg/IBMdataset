n = int(input())
A = [list(map(int, input().split())), list(map(int, input().split()))]
ans = 0
for i in range(n):
    ans = max(ans, sum(A[0][:i + 1]) + sum(A[1][i:]))
print(ans)
