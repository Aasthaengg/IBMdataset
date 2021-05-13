from collections import Counter

n = int(input())
a = list(map(int, input().split()))
q = int(input())
count_a = Counter(a)
total = sum(a)
nums = []
for i in range(q):
    b, c = map(int, input().split())
    if b in count_a:
        tmp = count_a[b]
    else:
        tmp = 0
    total = total - count_a[b] * b + tmp * c
    print(total)
    count_a[c] = count_a[c] + tmp
    count_a[b] = 0
