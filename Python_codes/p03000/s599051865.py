n, x = list(map(int, input().split()))
l = list(map(int, input().split()))
cnt = 1
x_idx = 0
for i in range(n):
    if (x_idx + l[i]) > x:
        break
    x_idx = x_idx + l[i]
    cnt += 1
print(cnt)