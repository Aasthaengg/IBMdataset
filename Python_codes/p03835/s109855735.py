# coding = SJIS

k, s = map(int, input().split())
ans = 0

for x in range(0, k + 1):
    for y in range(0, k + 1):
        z = s - x - y
        if 0 <= z and z <= k:
            ans += 1

print(ans)