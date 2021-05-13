#!/usr/bin/env python3

def main():
    N = int(input())
    a = [int(s) for s in input().split(' ')]

    result = []

    max_a = max(a)
    min_a = min(a)

    if 0 <= max_a + min_a:
        k = a.index(max_a)
        sk = str(k + 1) + ' '
        for i in range(N):
            if a[i] < 0:
                result.append(sk + str(i + 1))
        for i in range(1, N):
            result.append(str(i) + ' ' + str(i + 1))
    else:
        k = a.index(min_a)
        sk = str(k + 1) + ' '
        for i in range(N):
            if a[i] > 0:
                result.append(sk + str(i + 1))
        for i in range(N - 1, 0, -1):
            result.append(str(i + 1) + ' ' + str(i))

    print(len(result))
    for s in result:
        print(s)

if __name__ == '__main__':
    main()
