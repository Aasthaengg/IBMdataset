[r, c] = [int(x) for x in raw_input().split()]

A = []

counter = 0
while counter < r:
    raw = [int(x) for x in raw_input().split()]
    A.append(raw + [sum(raw)])
    counter += 1

A.append([sum([A[raw][col] for raw in range(r)]) for col in range(c + 1)])
for data in A:
    print(" ".join([str(x) for x in data]))