n, x, y = list(map(int, input().split()))

cnt = [0 for i in range(n-1)]
for i in range(1, n):
    for j in range(i+1, n+1):
        k = min(j - i, abs(x-i) + abs(y-j) + 1)
        cnt[k-1] += 1

for c in cnt:
    print(c) 