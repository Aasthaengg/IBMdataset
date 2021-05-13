N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
ref = K
while ref < N:
    ans += 1
    ref += K-1

print(ans)