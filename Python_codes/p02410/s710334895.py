# coding=utf-8

n, m = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in xrange(n)]
b = [input() for _ in xrange(m)]
Ab = [sum([A[i][j] * b[j] for j in xrange(m)]) for i in xrange(n)]
for x in Ab:
    print x