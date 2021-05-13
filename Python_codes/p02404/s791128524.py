from sys import stdin

while True:
    h, w = (int(n) for n in stdin.readline().rstrip().split())
    if h == w == 0:
        break

    for n in range(h):
        if n in {0, h - 1}:
            print('#' * w)
            continue

        print('#' + '.' * (w - 2) + '#')

    print()

