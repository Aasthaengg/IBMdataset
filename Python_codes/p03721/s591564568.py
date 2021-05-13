n, k = map(int, input().split())
A_MAX = 10**5
bkt = [0 for _ in range(A_MAX+1)]
for _ in range(n):
    a, b = map(int, input().split())
    bkt[a] += b
sum_count = 0
for i, cnt in enumerate(bkt):
    sum_count += cnt
    if sum_count >= k:
        print(i)
        break