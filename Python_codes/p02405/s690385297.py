from sys import stdin

for line in stdin:
    H, W = map(int, line.rstrip().split(' '))
    if 0 == H == W:
        break

    for i in range(H):
        for j in range(W):
            print('#' if (i+j)%2==0 else '.', end='')
        print()

    print()