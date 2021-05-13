from collections import Counter

H, W, N = [int(v) for v in input().split()]

square_list = []
for i in range(N):
    a, b = [int(v) for v in input().split()]
    for p in range(3):
        for q in range(3):
            if 1 <= a-p <= H-2 and 1 <= b - q <= W-2:
                square_list.append((a - p, b - q))

square_cnt = Counter(square_list)
ans = {i: 0 for i in range(10)}
ans[0] = (H-2) * (W-2) - len(square_cnt)
for cnt in square_cnt.values():
    ans[cnt] += 1

for k in sorted(ans.keys()):
    print(ans[k])