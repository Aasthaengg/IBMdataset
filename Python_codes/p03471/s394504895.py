N, Y = map(int, input().split())

q = Y//1000 - N

x = [0, 4, 8, 3, 7, 2, 6, 1, 5]

B = x.index(q%9)
b = B
while 4*b <= q:
    c = (q - 4*b) // 9
    a = N-c-b
    if a<0:
        b += 9
        continue
    else:
        print(c, b, a)
        break
else:
    print(-1, -1, -1)
