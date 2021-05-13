n = int(input())
k = int(input())
X = list(map(int, input().split()))
cnt = 0
for e in X:
    if e <= k // 2:
        cnt += e * 2
    else:
        cnt += (k - e) * 2
print(cnt)
