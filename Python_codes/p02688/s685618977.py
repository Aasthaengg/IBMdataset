n, k = map(int, input().split())
sunuke_set = set(i for i in range(1, n + 1))

for i in range(k):
    d = int(input())
    sunuke_list = list(map(int, input().split()))
    for sunuke in sunuke_list:
        sunuke_set.discard(sunuke)

print(len(sunuke_set))
