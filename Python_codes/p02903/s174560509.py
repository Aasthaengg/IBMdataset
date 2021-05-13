h, w, a, b = map(int, input().split())
result = ["0" * a + "1" * (w-a) for _ in range(b)] + ["1" * a + "0" * (w-a) for _ in range(h-b)]
for r in result:
    print(r)