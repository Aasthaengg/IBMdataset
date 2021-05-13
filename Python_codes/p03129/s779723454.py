N, K = map(int, input().split())
ans = 'YES' if K <= ((N >> 1) + (N & 1)) else 'NO'
print(ans)