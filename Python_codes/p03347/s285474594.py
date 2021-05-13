n = int(input())
prev = ans = -1
a = [int(input()) for _ in range(n)]
for i in a:
    if i - prev > 1:
        print(-1)
        exit()
    elif i - prev == 1:
        ans += 1
    else:
        ans += i
    prev = i
print(ans)