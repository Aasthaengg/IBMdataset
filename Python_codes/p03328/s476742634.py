a, b = map(int, input().split())

Tcum = [0] * (1000)
for i in range(999):
    Tcum[i+1] = Tcum[i] + (i+1)

print(Tcum[b-a]-b)