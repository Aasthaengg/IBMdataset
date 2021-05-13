# coding: utf-8

A, B, C, X = map(int, open(0).read().split())

count = 0

for a in range(0, A+1):
    for b in range(0, B+1):
        for c in range(0, C+1):
            money = 500 * a + 100 * b + 50 * c
            if money == X:
                count += 1

print(count)