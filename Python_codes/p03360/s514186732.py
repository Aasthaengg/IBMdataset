a, b, c = map(int, input().split())
k = int(input())
al = [a, b, c]
bl = [a, b, c]
cl = [a, b, c]

for i in range(k):
    al[0] = al[0] * 2
    bl[1] = bl[1] * 2
    cl[2] = cl[2] * 2

sm = [sum(al), sum(bl), sum(cl)]
print(max(sm))
