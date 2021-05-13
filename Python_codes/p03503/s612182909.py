def solve(bit):
    ret = 0
    for i in range(n):
        cnt = 0
        for j in range(10):
            if L[i][j] == bit[j] == 1:
                cnt += 1
        ret += p[i][cnt]
    return ret

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')
for i in range(1 << 10):
    bit = [0] * 10
    for j in range(10):
        if i >> j & 1:
            bit[j] = 1
    if 1 in bit:
        ans = max(ans, solve(bit))
print(ans)
