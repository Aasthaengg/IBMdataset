h, w = map(int, input().split())
a = [list(input().split()) for _ in range(h)]
print("#" * (w + 2))
for i in range(h):
    print("#" + a[i][0] + "#")
print("#" * (w + 2))
