from sys import stdin

while True:
    H, W = [int(x) for x in stdin.readline().rstrip().split()]
    if H == 0 and W == 0:
        break
    else:
        for i in range(H):
            for j in range(W):
                if (i+j)%2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                print()
        else:
            print()
