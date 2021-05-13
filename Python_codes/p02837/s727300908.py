import os, sys, re, math

N = int(input())
honest = []
liar = []

for i in range(N):
    a = int(input())
    h = []
    l = []
    for j in range(a):
        (x, y) = [int(n) for n in input().split()]
        if y == 1:
            h.append(x)
        else:
            l.append(x)
    honest.append(h)
    liar.append(l)

answer = 0
for i in range(2 ** N - 1, -1, -1):
    b = ('{:0%db}' % N).format(i)
    truth = True
    for j in range(N):
        if b[j] == '1':
            for h in honest[j]:
                if b[h - 1] != '1':
                    truth = False
                    break
            if not truth:
                break
            for l in liar[j]:
                if b[l - 1] != '0':
                    truth = False
                    break
        if not truth:
            break
    if truth:
        answer = max(answer, len(b.replace('0', '')))

print(answer)
