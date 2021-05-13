from sys import stdin
import math


N = int(stdin.readline().rstrip())

A=0
B=N-A


def sum_of_digit(n):
    total = 0
    s = str(n)
    for i in range(len(s)):
        total = total + int(s[i:i+1])

    return total


minimum = 9999999999

for a in range(1,N):
    a_total = sum_of_digit(a)
    b = N - a
    b_total = sum_of_digit(b)
    minimum = min(minimum, a_total + b_total)

print(minimum)
