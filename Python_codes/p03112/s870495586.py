import bisect
import sys
input = sys.stdin.readline

A, B, Q = map(int, input().split())
Shrine = [int(input()) for _ in range(A)]
Temple = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]
Shrine = [-100000000000] + Shrine + [100000000000]
Temple = [-100000000000] + Temple + [100000000000]

for x in X:
    nums = bisect.bisect_left(Shrine, x)
    tems = bisect.bisect_left(Temple, x)
    ans1 = max(abs(Shrine[nums]-x), abs(Temple[tems]-x))
    ans2 = max(abs(x - Shrine[nums-1]), abs(x - Temple[tems-1]))
    ans3 = abs(Shrine[nums]-x) * 2 + abs(x - Temple[tems-1])
    ans4 = abs(Temple[tems]-x) * 2 + abs(x - Shrine[nums-1])
    ans5 = abs(x - Shrine[nums-1]) * 2 + abs(Temple[tems]-x)
    ans6 = abs(x - Temple[tems-1]) * 2 + abs(Shrine[nums]-x)

    print(min(ans1, ans2, ans3, ans4, ans5, ans6))