h, w, a, b = map(int, input().split())
for i in range(b):
    l = ["0"] * a + ["1"] * (w-a)
    print("".join(l))
for i in range(h-b):
    l = ["1"] * a + ["0"] * (w-a)
    print("".join(l))