_ = input()
a = [int(x) for x in input().split()]

p = [False] * 8
q = 0
for i in a:
    if 3199 < i:
        q += 1
    else:
        for j in range(8):
            if 400 * j <= i < 400 * (j + 1):
                p[j] = True
else:
    s = sum(p)
    print(max(s, 1), s + q)