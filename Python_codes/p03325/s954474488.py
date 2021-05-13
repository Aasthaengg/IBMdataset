from math import log2
n = int(input())
a = list(map(int, input().split()))
ans = 0

for _a in a:
    if _a%2 == 0:
        cnt =0
        while _a%2 == 0:
            _a //= 2
            cnt += 1
        ans += cnt

print(int(ans))