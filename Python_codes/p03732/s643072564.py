from itertools import accumulate
N, W = map(int, input().split())
Items = [[] for i in range(4)]

w, v = map(int, input().split())
base_w = w
Items[0].append(v)

for i in range(N - 1):
    w, v = map(int, input().split())
    Items[w - base_w].append(v)

for i in range(4):
    Items[i] = [0] + sorted(Items[i], reverse=True)
    Items[i] = list(accumulate((Items[i])))


ans = 0
for w0 in range(len(Items[0])):
    for w1 in range(len(Items[1])):
        for w2 in range(len(Items[2])):
            for w3 in range(len(Items[3])):
                if base_w * w0 + (base_w + 1) * w1 + (base_w + 2) * w2 + (base_w + 3) * w3 > W:
                    continue
                tmp_ans = Items[0][w0] + Items[1][w1] + Items[2][w2] + Items[3][w3]
                ans = max(ans, tmp_ans)

print(ans)
