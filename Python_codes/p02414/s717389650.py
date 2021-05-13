[n, m, l] = [int(x) for x in raw_input().split()]

A = []
B = []
counter = 0
while counter < n:
    A.append([int(x) for x in raw_input().split()])
    counter += 1

counter = 0
while counter < m:
    B.append([int(x) for x in raw_input().split()])
    counter += 1

B = list(zip(*B))

for i in range(n):
        print(' '.join([str(x) for x in [sum([x[0] * x[1] for x in zip(A[i], B[j])]) for j in range(l)]]))