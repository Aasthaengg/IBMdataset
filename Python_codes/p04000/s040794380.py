import collections
H, W, N = map(int, input().split())

delta = (-1, 0, 1)

ans = []
for i in range(N):
    a, b = map(int, input().split())
    for da in delta:
        for db in delta:
            if 1 <= a-1+da <= H-2 and 1 <= b-1+db <= W-2:
                ans.append((a-1+da, b-1+db))

cc = collections.Counter(collections.Counter(ans).values())
zc = (H-2)*(W-2)-sum(cc.values())
print(zc)
for i in range(1, 10):
    print(cc[i])
