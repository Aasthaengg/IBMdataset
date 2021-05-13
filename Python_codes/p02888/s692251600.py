from bisect import bisect_left, bisect_right

n = int(input())
l = list(map(int, input().split()))
l.sort()
pattern = 0
for i in range(n - 2):
    a = l[i]
    for j in range(i + 1, n - 1):
        b = l[j]
        c_idx = bisect_left(l, a + b)
        pattern += (c_idx - j - 1)
print(pattern)
