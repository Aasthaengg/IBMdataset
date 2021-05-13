N, *V, = map(int, open(0).read().split())

V.sort(reverse=True)

while True:
    if len(V) == 1:
        break
    V.append((V.pop() + V.pop()) / 2)

print(V[0])