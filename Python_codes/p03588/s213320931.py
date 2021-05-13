n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

i = a.index(max(a))
print(max(a)+b[i])
