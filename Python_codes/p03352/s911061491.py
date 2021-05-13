x = int(input())
ans = 1
for b in range(1,x):
    for p in range(2,x):
        a = b**p
        if a == a // 1 and a > ans and a <= x:
            ans = a
        if a>x:
            break
    if a > x:
        continue
print(ans)
