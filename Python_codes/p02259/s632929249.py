# -*- coding: utf-8 -*-


def bubble_sort(a, N):
    change = 0
    for i in xrange(N - 1):
        for j in xrange(N - 1, i, -1):
            if a[j - 1] > a[j]:
                temp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = temp
                change += 1
    return (a, change)


if __name__ == "__main__":
    N = input()
    a = map(int, raw_input().split())
    result, change = bubble_sort(a, N)
    print ' '.join(map(str, result))
    print change