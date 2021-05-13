n, a, b = map(int, raw_input().split())
X = map(int, raw_input().split())
energy = 0
for i in range(n-1):
    if (X[i+1] - X[i]) * a < b:
        energy += (X[i+1]-X[i]) * a
    else:
        energy += b
print energy