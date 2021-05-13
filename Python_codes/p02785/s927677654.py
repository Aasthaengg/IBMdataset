n, k = map(int, input().split())
hp = sorted(list(map(int, input().split())))
for _ in range(min(len(hp), k)):
    del hp[-1]
print(sum(hp))