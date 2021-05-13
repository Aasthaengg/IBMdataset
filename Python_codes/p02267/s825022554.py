# -*- coding: utf-8 -*-


def linerSearch(S, key):
    i = 0
    S.append(key)
    while S[i] != key:
        i += 1
    if i == len(S)-1:
        S.pop()
        return False
    S.pop()
    return True

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0

for i in range(q):
    if linerSearch(S, T[i]):
        count += 1

print (count)