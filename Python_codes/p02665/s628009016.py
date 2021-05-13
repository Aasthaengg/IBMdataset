N = int(input())
A = list(map(int, input().split()))

ans, cnt, node = 0, sum(A), 1
for i in range(N + 1):
    ans += node
    cnt -= A[i]
    node = min(cnt, (node - A[i]) * 2)
    if node < 0:
        print(-1)
        break
else:
    print(ans)

