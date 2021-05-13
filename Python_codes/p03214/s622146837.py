from sys import stdin
N = int(stdin.readline().rstrip())
a = [int(_) for _ in stdin.readline().rstrip().split()]
avg = sum(a) / len(a)
ans_idx = 0
ans_f = 101
for i, f in enumerate(a):
    diff = abs(f-avg)
    if diff < ans_f:
        ans_f = diff
        ans_idx = i
print(ans_idx)