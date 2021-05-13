import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

r = 0
l = 1e9

test_count = 0

while (l - r > 1) :
    target_log_len = (r + l) // 2
    cut_count = 0

    for log_len in A:
        cut_count += (log_len - 1) // target_log_len

    if cut_count <= K:
        l = target_log_len
    else:
        r = target_log_len

    test_count += 1
    if test_count > 100:
        break

print(int(l))