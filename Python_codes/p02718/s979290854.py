n, m = map(int, input().split())
a = list(map(int, input().split()))

a_thr = sum(a) / (4 * m)
count = 0
for a_i in a:
    if a_i >= a_thr:
        count += 1
print('Yes' if count >= m else 'No')
