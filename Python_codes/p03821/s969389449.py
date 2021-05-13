N, *AB = [map(int, s.split()) for s in open(0)]
AB = list(AB)[::-1]
bias = 0
for A, B in AB:
    bias += (bias + A + B - 1) // B * B - A - bias
print(bias)
