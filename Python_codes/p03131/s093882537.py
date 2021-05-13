#!/usr/bin/env python3

K, A, B = map(int, input().split())

tataku = A - 1
if (A > B) or (A >= K) or (A + 1 == B): #  or (tataku + 1 >= K):
    print(K+1)
else:
    c = B
    nokori = K - tataku - 2
    if nokori % 2 == 1:
        c += (B-A) * (nokori//2) + 1
    else:
        c += (B-A) * (nokori//2)

    print(c)

