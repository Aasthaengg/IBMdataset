# coding: utf-8

a, b = list(map(int, input().strip().split()))
print(' '.join(map(str, [a * b, 2 * (a + b)])))