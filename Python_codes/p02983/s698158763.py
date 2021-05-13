m, n = map(int, input().split(" "))
if n - m >= 673:
    print(0)
else:
    score = m * n % 2019
    for i in range(m, n + 1):
        for j in range(i + 1, n + 1):
            if (i * j) % 2019 < score:
                score = (i * j) % 2019
    print(score)
