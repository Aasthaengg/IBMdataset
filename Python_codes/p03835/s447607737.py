K, S = [int(x) for x in input().split()]

ans = 0
for i in range(K + 1):
    for j in range (K + 1):
        r = S - i - j
        if r <= K and r >= 0:
            ans += 1
        
print(ans)       