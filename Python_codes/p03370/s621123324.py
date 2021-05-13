n, x = map(int, input().split())
cnt = 0

m = [int(input()) for _ in range(n)]
M = sorted(m)
if sum(m) <= x:
    cnt += (n +(x - sum(m)) // min(m))
else:
    while x >= 0:
        for i in range(n):
            x -= M[i]
            cnt += 1
print(cnt)