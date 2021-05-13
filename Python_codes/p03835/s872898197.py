K, S = map(int, input().split())
count = 0
for x in range(K+1):
    for y in range(min(S-x+1, K+1)):
        if S - x - y <= K:
            count += 1
print(count)