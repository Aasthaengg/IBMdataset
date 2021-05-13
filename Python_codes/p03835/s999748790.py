K, S = list(map(int, input().split()))
ct = 0
for a in range(K+1):
    for b in range(K+1):
        if S-K <= a+b <= S:
            ct += 1
print(ct)