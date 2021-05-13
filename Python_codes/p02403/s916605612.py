import sys
while True:
    (H, W) = [int(i) for i in sys.stdin.readline().split()]
    if H == W == 0:
        break
    print(("#" * W + "\n") * H)