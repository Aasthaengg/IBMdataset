n = int(input())
for h in range(max(1, int(n / 4)), min(3500, int(3*n / 4)) + 1):
    for w in range(max(1, int(3*n / 4)), 3501):
        num = n * h * w
        den = 4 * h * w - n * (h + w)
        if den != 0 and num % den == 0 and h <= num // den <= w:
            print(h, num // den, w)
            exit()