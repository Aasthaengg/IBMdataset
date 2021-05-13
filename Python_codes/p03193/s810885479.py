n, h0, w0 = map(int, input().split())
count = 0
for i in range(n):
    h, w = map(int, input().split())
    if h >= h0 and w >= w0:
        count += 1

print(count)

