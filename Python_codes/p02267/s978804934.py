# coding=utf-8

n = int(input())
S = list(map(int, input().split()))
q = int(input())
counter = 0

for t in map(int, input().split()):
    if t in S:
        counter += 1

print(counter)