n = int(input())
a = [0] + list(map(int, input().split())) + [0]
origin_len = 0
for i in range(n+1):
    origin_len += abs(a[i] - a[i+1])

for i in range(n):
    if a[i] <= a[i+1] <= a[i+2] or a[i+2] <= a[i+1] <= a[i]:
        print(origin_len)
    else:
        len_a = abs(a[i+1] - a[i])
        len_b = abs(a[i+1] - a[i+2])

        print(origin_len - 2 * min(len_a, len_b))