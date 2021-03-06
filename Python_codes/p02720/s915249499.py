#!/usr/bin/env python3
def main():
    def rec(d: int, val: int, all: list):
        all.append(val)
        if d == 10:
            return
        for j in range(-1, 2):
            add = (val % 10) + j
            if add >= 0 and add <= 9:
                rec(d + 1, val * 10 + add, all)
    
    K = int(input())

    all = []
    for v in range(1, 10):
        rec(1, v, all)
    print(sorted(all)[K - 1])


if __name__ == '__main__':
    main()
