n = int(input())
L = [2, 1]
for _ in range(n-1):
    L.append(sum(L[-2:]))
print(L[-1])