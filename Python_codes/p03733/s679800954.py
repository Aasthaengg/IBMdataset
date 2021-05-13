n, T = list(map(int, input().split()))

t = list(map(int, input().split()))

cnt = n*T
for i in range(1, n):
    diff = t[i]-t[i-1]
    if diff < T:
        cnt -= T-diff

print(cnt)