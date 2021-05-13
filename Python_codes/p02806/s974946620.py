n = int(input())
st = [list(input().split()) for _ in range(n)]
x = input()

ans = 0
mode = 0
for s, t in st:
    if mode == 0:
        if s == x:
            mode = 1
    else:
        ans += int(t)

print(ans)