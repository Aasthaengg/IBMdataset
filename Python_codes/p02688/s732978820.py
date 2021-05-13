n, k = map(int, input().split())
sunuke_set = set(i for i in range(1, n + 1))

for i in range(k):
    d = int(input())
    sunuke_tuple = tuple(map(int, input().split()))
    for sunuke in sunuke_tuple:
        sunuke_set.discard(sunuke)

print(len(sunuke_set))
