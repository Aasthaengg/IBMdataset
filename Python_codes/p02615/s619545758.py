import math

n = int(input())
players = [int(x) for x in input().split()]
players.sort(reverse = True)
comfortness = 0
for i in range(n-1):
    comfortness += players[math.ceil(i/2)]

print(comfortness)