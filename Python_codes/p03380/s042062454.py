n = int(input())
a = list(map(int, input().split()))
n = max(a)
tmp = n / 2
r = n + 1
d = n + 1
for num in a:
    if num == n:
        continue
    d_tmp = abs(num - tmp)
    if d_tmp < d:
        d = d_tmp
        r = num
print(n, r)