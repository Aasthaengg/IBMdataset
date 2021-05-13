h, w, a, b = map(int, input().split())

s = [["1"] * a + ["0"] * (w - a) for _ in range(b)] + [["0"] * a + ["1"] * (w - a) for _ in range(h - b)]

for x in s:
    print("".join(x))