N = int(input())
vA = list(map(int, input().split()))

aveA = sum(vA) / N
vD = [abs(a - aveA) for a in vA]

res = vD.index(min(vD))
print(res)
