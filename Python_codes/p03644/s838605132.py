n = int(input())
if n == 1:
    print(1)
else:
    times = []
    for i in range(2, n + 1, 2):
        t = 0
        while i % 2 == 0:
            i //= 2
            t += 1
        else:
            times.append(t)
    else:
        print((times.index(max(times)) + 1) * 2)