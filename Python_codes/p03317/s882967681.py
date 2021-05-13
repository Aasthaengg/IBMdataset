N, K = map(int, input().split())
A = list(map(int, input().split()))
N -= K
K -= 1
ans = 1
ans += (N-1)//K + 1
print(ans)
