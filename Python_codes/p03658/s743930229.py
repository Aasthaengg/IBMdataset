N, K = map(int, input().split())
L = [int(i) for i in input().split()]
sorted_L = sorted(L, reverse=True)

max = 0
for i in range(K):
    max += sorted_L[i]

print(max)