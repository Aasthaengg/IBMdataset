def kaijou(num):
    wa = 0
    for i in range(num, 0, -1):
        wa += i
    return wa
a, b = map(int, input().split())
dst = kaijou(b-a) - b
print(dst)
