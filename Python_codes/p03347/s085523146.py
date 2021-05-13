N = int(input())
src = [int(input()) for i in range(N)]
if src[0]:
    print(-1)
    exit()

ans = prev = 0
for a in reversed(src):
    if prev > 0:
        if a == prev - 1:
            prev = a
            continue
        elif a < prev:
            print(-1)
            exit()
    ans += a
    prev = a
print(ans)
