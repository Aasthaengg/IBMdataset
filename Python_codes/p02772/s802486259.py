import os, sys, re, math

N = int(input())
A = [int(n) for n in input().split()]

answer = 'APPROVED'
for a in A:
    if a % 2 == 0:
        if not (a % 3 == 0 or a % 5 == 0):
            answer = 'DENIED'
            break

print(answer)
