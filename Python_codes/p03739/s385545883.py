N = int(input())
A = [int(_) for _ in input().split()]
now = 0
cnt = 0
for i, a in enumerate(A):
    b = (-1)**i
    now += a
    if now * b <= 0:
        cnt += abs(now - b)
        now = b
ans = cnt
now = 0
cnt = 0
for i, a in enumerate(A):
    b = (-1)**(i + 1)
    now += a
    if now * b <= 0:
        cnt += abs(now - b)
        now = b
ans = min(ans, cnt)
print(ans)
