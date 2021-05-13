n,d = map(int, input().split())
cnt = 0

for i in range(n):
    x,y = map(int, input().split())
    t = (x**2 + y**2) ** 0.5

    cnt += t <= d

print(cnt)