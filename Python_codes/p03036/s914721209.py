r, D, x = map(int, input().split())
out = x
for y in range(10):
    out = r * out - D
    print(out)
