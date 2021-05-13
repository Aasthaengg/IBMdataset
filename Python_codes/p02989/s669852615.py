n = int(input())
d = sorted(list(map(int, input().split())))
half = n // 2
print(d[half] - d[half - 1])