a, b, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

payl = []
nom = min(al) + min(bl)
payl.append(nom)

for i in range(m):
    ml = list(map(int, input().split()))
    payl.append(al[ml[0] - 1] + bl[ml[1] - 1] - ml[2])

print(min(payl))