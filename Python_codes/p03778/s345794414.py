W, a, b = map(int, input().split())

l = min([a, b])
r = max([a, b])

if l+W <= r:
    print(r-(l+W))
else:
    print(0)
