h, w, a, b = map(int, input().split())
print(
    *(
        ["0" * a + "1" * (w - a) for _ in range(b)]
        + ["1" * a + "0" * (w - a) for _ in range(h - b)]
    ),
    sep="\n"
)
