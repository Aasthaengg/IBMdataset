N = int(input())
b = list(map(lambda s: int(s) - 1, input().split()))

ops = []

for i in range(N, 0, -1):
    for j in range(i - 1, -1, -1):
        if b[j] == j:
            ops.append(j)
            b = b[:j] + b[j + 1:]
            break
    else:
        ops = [-2]
        break

for i in range(len(ops) - 1, -1, -1):
    print(ops[i] + 1) # 1-based indexing