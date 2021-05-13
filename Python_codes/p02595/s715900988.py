N, D = map(int, input().split(" "))
cnt = 0
for _ in range(N):
    x, y = map(int, input().split(" "))
    r = (x**2+y**2)**0.5
    if D >= r:
        cnt += 1
print(cnt)