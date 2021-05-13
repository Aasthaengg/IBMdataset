def flip(c):
    return '#' if c == '.' else '.'

while True:
    H, W = [int(x) for x in input().strip().split(' ')]
    if H == 0 and W == 0:
        break
    for i in range(H):
        start = '#' if i % 2 == 0 else '.'
        l = ''
        for j in range(W):
            p = start if j % 2 == 0 else flip(start)
            l += p
        print(l)
    print('')