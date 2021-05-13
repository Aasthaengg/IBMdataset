# -*- coding: utf-8 -*-
N, X = [int(n) for n in input().split()]
l = [int(n) for n in input().split()]

D = [0]
for i in range(N):
    D.append(D[-1] + l[i])

#print(D)

count = 0
for n in D:
    if n <= X:
        count += 1
    else:
        break

print(count)