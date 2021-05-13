X = int(input())
ans = 0
p = 100
for i in range(1, 100000):
    p += p // 100
    if p>=X:
        ans = i
        break
print(ans)