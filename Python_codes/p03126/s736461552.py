n, m = map(int, input().split())
ans = set()
for i in range(n):
    ka = list(map(int, input().split()))
    a = set(ka[1:])
    if i == 0:
        ans = a
    else:
        ans = ans & a
print(len(ans))