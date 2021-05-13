n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
a.sort()
for num in a:
    if x >= num:
        ans += 1
        x -= num
    else:
        break
else:
    if x == 0:
        print(ans)
    else:
        print(ans - 1)
    exit()
print(ans)