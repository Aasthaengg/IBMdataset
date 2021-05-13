n = int(input())
Z = [0 for i in range(n)]
W = [0 for i in range(n)]
for i in range(n):
    xi, yi = map(int, input().split())
    Z[i] = xi + yi
    W[i] = xi - yi

ans = max(max(Z)-min(Z), max(W)-min(W))
print(ans)