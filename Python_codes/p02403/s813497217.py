from sys import stdin

for line in stdin:
    H, W = map(int, line.rstrip().split(' '))
    if 0 == H == W:
        break

    for i in range(H):
        print('#'*W)
    print()