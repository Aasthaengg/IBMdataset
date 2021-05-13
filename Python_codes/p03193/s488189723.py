n, h, w = map(int, input().split())
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if h <= a and w <= b:
        cnt += 1
    else:
        continue
print(cnt)