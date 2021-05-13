import sys
while True:
    (H, W) = [int(i) for i in sys.stdin.readline().split()]
    if H == W == 0:
        break
    print("#" * W)
    print(("#" + "." * (W - 2) + "#" + "\n") * (H - 2), end="")
    print("#" * W + "\n")