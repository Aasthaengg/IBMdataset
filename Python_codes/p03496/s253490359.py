#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    absmaxindex = 0
    for i in range(1, n):
        if abs(a[i]) > abs(a[absmaxindex]):
            absmaxindex = i

    print(2 * n - 2)
    for i in range(n):
        if i == absmaxindex:
            continue
        print(absmaxindex + 1, i + 1)
    if a[absmaxindex] >= 0:
        for i in range(n - 1):
            print(i + 1, i + 2)
    else:
        for i in reversed(range(n - 1)):
            print(i + 2, i + 1)

if __name__ == "__main__":
    main()
