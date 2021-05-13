# 171 B
N, K = list(map(int, input().split()))
P = list(map(int, input().split()))
P.sort()
ans = 0
for i in range(0, K):
    ans += P[i]
    
print(ans)