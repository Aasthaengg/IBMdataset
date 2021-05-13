N, K = map(int, input().split())
A = list(map(int, input().split()))

# 並び順を変えても普遍
ans = 0
i = 0

while True:
    if i*(K-1) >= N-1:
        break
    ans += 1
    i += 1
    
print(ans)