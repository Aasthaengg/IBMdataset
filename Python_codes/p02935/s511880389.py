N = int(input())
V = list(map(int, input().split()))
V.sort()
res = V[0]
for v in V[1:]:
    res = (res + v)/2
print(res)