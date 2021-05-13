import sys
input = sys.stdin.buffer.readline

MOD = 10**9+7

n = int(input())
a = list(map(int, input().split()))

rgb = [0, 0, 0]

ans = 1
for i in range(n):
    ans *= rgb.count(a[i])
    ans %= MOD
    # print(rgb, a[i], ans)
    for j in range(3):
        if rgb[j] == a[i]:
            rgb[j] += 1
            break
print(ans)
