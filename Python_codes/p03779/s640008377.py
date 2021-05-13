x = int(input())

for t in range(int(1e5)):
    s = (t + 1) * t / 2
    if s >= x:
        print(t)
        exit()
