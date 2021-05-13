vs = sorted(list(map(int, input().split())))
for v in vs:
    end = '\n' if v == vs[-1] else ' '
    print(v, end=end)

