# coding: utf-8

N = int(input())
S = input()

east = S.count("E")
west = 0


res = 1000000
for i in range(len(S)):
    if S[i] == "E":
        east -= 1
    res = min(res, east + west)
    if S[i] == "W":
        west += 1

print(res)
