n = int(input())
ans = -1
prev = -1
for _ in range(n):
    a = int(input())
    if prev+1 == a:
        prev = a
        ans += 1
        continue
    if prev+1 < a:
        print(-1)
        break
    ans += a
    prev = a
else:
    print(ans)
