k = int(input())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
elif k == 1 or k == 7:
    print(1)
else:
    t = 2
    ex = 77
    for i in range(10 ** 8):
        if ex % k == 0:
            break
        ex = (ex % k) * 10 + 7
        t += 1
    print(t)