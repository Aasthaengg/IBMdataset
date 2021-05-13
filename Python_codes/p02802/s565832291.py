import os, sys, re, math

(N, M) = [int(n) for n in input().split()]

successes = [0] * N
penalties = [0] * N
for i in range(M):
    (p, s) = [n for n in input().split()]
    if s == 'AC':
        successes[int(p) - 1] = 1
    else:
        if successes[int(p) - 1] == 0:
            penalties[int(p) - 1] += 1

for i in range(N):
    if successes[i] == 0:
        penalties[i] = 0

print('%s %s' % (sum(successes), sum(penalties)))
