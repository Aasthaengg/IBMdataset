N, H, W = map(int, input().split())
p = 0
for _ in range(N):
    a, b = map(int, input().split())
    if H <= a and W <= b:
        p += 1
print(p)