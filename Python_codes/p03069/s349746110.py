import sys
N = int(sys.stdin.readline().rstrip())
S = list(sys.stdin.readline().rstrip())

count = []
cnt_b = 0
cnt_w = 0
for s in S:
    if s == "#":
        cnt_b += 1
    else:
        cnt_w += 1
    count.append((cnt_b, cnt_w))

ans_1 = N - cnt_b
ans_2 = N - cnt_w
ans_3 = float("inf")

for i, j in count:
    ans_3 = min(ans_3, i + cnt_w - j)

print(min(ans_1, ans_2, ans_3))