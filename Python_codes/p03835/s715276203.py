k, s = list(map(int, input().split()))
count = 0

for p in range(k+1):
    for q in range(k+1):
        r = s-p-q
        if r>=0 and r<=k:
            count += 1

print(count)
