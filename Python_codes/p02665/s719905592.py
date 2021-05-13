N = int(input())
A = list(map(int, input().split()))

ans = 0

leaves = sum(A)
node_num = 1

for i in range(N+1):
    if A[i] > node_num:
        print(-1)
        exit()
    ans += min(node_num, leaves)

    leaves -= A[i]
    node_num -= A[i]
    node_num *= 2
print(ans)

