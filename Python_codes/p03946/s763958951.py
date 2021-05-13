N, T = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

max_diff = 0
cnt = 0
min_a = A[0]
for i in range(1, N):
    a = A[i]
    if min_a > a:
        min_a = a
        continue

    if max_diff < a - min_a:
        max_diff = a - min_a
        cnt = 1
    elif max_diff == a - min_a:
        cnt += 1
print(cnt)
