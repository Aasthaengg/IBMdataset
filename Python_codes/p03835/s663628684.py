K, S = map(int, input().split())
count = 0
for x in range(K+1):
    if K < 1/2 * (S - x):
        continue
    for y in range(min(S - x + 1, K + 1)):
        if K < (S - x - y):
            continue
        else:
            count += 1
print(count) 