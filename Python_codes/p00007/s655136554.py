#!/usr/bin/env python3
def main():
    N = int(input())
    c = 100000
    for _ in range(N):
        c *= 1.05
        t = c % 1000
        if t > 0:
            c += 1000 - t
    print(int(c))

if __name__ == "__main__":
    main()