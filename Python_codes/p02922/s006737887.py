A, B = map(int, input().strip().split(" "))

if B == 1:
    print(0)
else:
    socks = 1
    taps = 0
    while socks < B:
        socks -= 1
        socks += A
        taps += 1
    print(taps)