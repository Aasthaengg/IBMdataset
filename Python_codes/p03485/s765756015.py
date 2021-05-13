a,b = map(int, input().split())
mean = (a+b) / 2
if mean // 1 == mean:
    print(int(mean))
else:
    print(int(mean//1) + 1)