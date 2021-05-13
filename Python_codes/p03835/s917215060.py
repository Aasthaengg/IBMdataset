K, S = map(int, input().split())

success = 0

for x in range (K + 1):
    for y in range (K + 1):
        if S - x - y >= 0 and S - x - y <= K:
            success = success + 1

print(success)
