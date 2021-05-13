W, H, N = map(int, input().split())
a1, a2, a3, a4 = [], [], [], []
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        a1.append(x)
    elif a == 2:
        a2.append(x)
    elif a == 3:
        a3.append(y)
    else:
        a4.append(y)

max_x = max(a1) if a1 else 0
min_x = min(a2) if a2 else W
max_y = max(a3) if a3 else 0
min_y = min(a4) if a4 else H
ans = max(0, min_x - max_x) * max(0, min_y - max_y)
print(ans)