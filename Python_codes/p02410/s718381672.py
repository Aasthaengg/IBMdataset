# coding=utf-8

A = []
n, m = map(int, raw_input().split())
for _ in xrange(n):
    A.append(map(int, raw_input().split()))
# print A

b = []
for _ in xrange(m):
    b.append(input())
# print b

Ab = [sum([A[i][j] * b[j] for j in xrange(m)]) for i in xrange(n)]
# print Ab
for x in Ab:
    print x