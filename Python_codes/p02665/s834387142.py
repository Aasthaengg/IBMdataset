N = int(input())
A = list(map(int, input().split()))
flg = True
n_node = 0.5
ans = 0
As = [0]*(N+2)
for i in range(N, -1, -1):
    As[i] = As[i+1] + A[i]
for i in range(N+1):
    if A[i] > n_node*2:
        flg = False
        break
    n_node = min(int(n_node*2)-A[i], As[i+1])
    ans += n_node + A[i]
print(ans if flg else -1)
