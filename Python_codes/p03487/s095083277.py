from collections import Counter
n = int(input())
a=[int(i) for i in input().split()]
a = Counter(a)
cnt = 0
for key in a.keys():
    val = a[key]
    if key>val:
        cnt += val
    else:
        cnt += abs(val-key)
print(cnt)