x, a, b = list(map(int, input().split()))

ad = abs(x-a)
bd = abs(x-b)

if ad<bd:
    print("A")
else:
    print("B")