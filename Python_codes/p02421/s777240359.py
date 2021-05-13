# coding: utf-8

n = int(raw_input())
scores = [0,0]
for i in range(n):
    tarou, hanako = raw_input().split()
    if tarou > hanako:
        scores[0] += 3
    elif tarou < hanako:
        scores[1] += 3
    else:
        scores[0] += 1
        scores[1] += 1

print scores[0], scores[1]