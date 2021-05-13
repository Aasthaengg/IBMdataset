N = int(input())
lucas = [2, 1]
for n in range(2, N + 1):
    lucas += [lucas[-1] + lucas[-2]]
print(lucas[-1])