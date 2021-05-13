A, B, C, D, E, F = map(int, input().split())

water = set()
sugar = set()

for i in range(0, F+1, 100*A):
    for j in range(0, F+1-A, 100*B):
        water.add(i+j)

for i in range(0, F+1, C):
    for j in range(0, F+1-C, D):
        sugar.add(i+j)

per = -1
for w in water:
    for s in sugar:
        ws = w+s
        # 砂糖水の質量合計はFg以下 and 砂糖が溶け残らない
        if 0 < ws <= F and s <= w*E // 100:
            if s/(ws) > per:
                per = s/(ws)
                ans = ws, s

print(ans[0], ans[1])