#!/usr/bin/env python

if __name__ == '__main__':
    n = int(raw_input())
    X = map(int, raw_input().split())
    Y = map(int, raw_input().split())

    dist = []
    for i in range(n):
        dist += [abs(X[i]-Y[i])]

    print sum(dist)
    print sum(map(lambda x : x**2, dist))**(1.0/2)
    print sum(map(lambda x : x**3, dist))**(1.0/3)
    print max(dist)

