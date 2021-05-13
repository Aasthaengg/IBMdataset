a, b = map(int, input().split())

High = [1]
for i in range(998):
    High.append(High[-1] + i+2)

A = []
for h1, h2 in zip(High, High[1:]):
    A.append(h2 - h1)
    if h2 - h1 == b - a:
        print(h1-a)
        exit()
