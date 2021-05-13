# coding=utf-8

a, b = map(int, raw_input().split())
print "{0:d} {1:d} {2:f}".format(a / b, a % b, 1.0 * a / b)