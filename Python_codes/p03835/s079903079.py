K, S = map(int, input().split())
n = 0
for x in range(K + 1):
    for y in range(K + 1):
        if 0 <= S - (x + y) and S - (x + y) <= K:
            n += 1
print(n)