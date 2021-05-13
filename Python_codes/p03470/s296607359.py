import sys

n = int(input())
d = [int(input()) for i in range(n)]

dan = len(list(set(d)))
print(dan)