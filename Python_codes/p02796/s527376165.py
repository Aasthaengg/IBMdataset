n = int(input())
xl = []
for i in range(n):
    l, r = map(int, input().split())
    xl.append([l-r, l+r])
xl.sort(key=lambda x: x[1])
ans = 0
inf = 10 ** 10
prev_r = - inf
for l, r in xl:
    if prev_r > l:
        continue
    ans += 1
    prev_r = r
print(ans)
