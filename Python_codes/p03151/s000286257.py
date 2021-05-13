N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) < sum(B):
    print(-1)
    exit()
neg_diffs = []
pos_diffs = []
for a, b in zip(A, B):
    if a < b:
        neg_diffs.append(b - a)
    else:
        pos_diffs.append(a - b)
if len(pos_diffs) == N:
    print(0)
    exit()
cnt = 0
neg_sum = sum(sorted(neg_diffs))
for pos_diff in sorted(pos_diffs, reverse=True):
    if neg_sum <= 0:
        break
    neg_sum -= pos_diff
    cnt += 1
print(cnt + len(neg_diffs))
