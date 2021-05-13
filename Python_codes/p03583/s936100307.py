N = int(input())
end = False
for h in range(1, 3501):
    if end:
        break
    for n in range(1, 3501):
        if (4 * h * n - N * n - N * h):
            if (N * h * n) % (4 * h * n - N * n - N * h) == 0:
                w = (N * h * n) // (4 * h * n - N * n - N * h)
                if w > 0:
                    print(h, n, w)
                    end = True
                    break