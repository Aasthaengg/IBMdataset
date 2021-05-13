n = int(input())
p = list(map(int, input().split()))

cnt = 0
for i, c in enumerate(p):
    if i == 0 or i == n-1:
        continue
    if p[i + 1] > p[i] > p[i - 1] or p[i - 1] > p[i] > p[i + 1]:
        cnt += 1

print(cnt)