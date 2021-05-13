#!/usr/bin/env python3
def main():
    A, B = map(int, input().split())

    for price in [str(x) for x in range(10, 1001)]:
        a = str(int(price) * 8)
        a = int(a[:-2]) if len(a) >= 3 else 0
        b = int(price[:-1]) if len(price) >= 2 else 0
        if a == A and b == B and a <= 100 and b <= 100:
            print(price)
            return
    print(-1)


if __name__ == '__main__':
    main()
