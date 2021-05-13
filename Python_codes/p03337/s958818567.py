A, B = [int(i) for i in input().split()]

results = []

results.append(A + B)
results.append(A - B)
results.append(A * B)

print(max(results))