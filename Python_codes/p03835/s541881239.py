K, S = map(int, input().split())
c = 0
for x in range(K + 1):
    if x > S:
        break
    for y in range(S - x + 1):
        if y > K:
            break
        z = S - x - y
        if 0 <= z <= K:
            c += 1
print(c)