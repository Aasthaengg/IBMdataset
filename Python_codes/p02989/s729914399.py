N = int(input())
d = sorted(list(map(int, input().split())))

num = d[N // 2 - 1]
ans = 0
for i in range(10**5):
    num += 1
    if d[N // 2 - 1] < num <= d[N//2]:
        ans += 1
    if num > d[N//2]:
        break
print(ans)
