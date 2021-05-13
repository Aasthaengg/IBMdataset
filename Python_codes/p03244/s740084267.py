from collections import Counter
n = int(input())
v = input().split()

if len(set(v)) == 1:
    print(n // 2)
else:
    c1 = Counter(v[::2])
    c2 = Counter(v[1::2])
    c1m = c1.most_common()
    c2m = c2.most_common()

    if c1m[0][0] == c2m[0][0]:
        print(min(n - c1m[0][1] - c2m[1][1], n - c1m[1][1] - c2m[0][1]))
    else:
        print(n - c1m[0][1] - c2m[0][1])