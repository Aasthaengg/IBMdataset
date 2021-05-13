n, c, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
l = sorted(l)
val, ans = l[0], 1
count = 1
for i in l[1:]:
    count += 1
    if i-val > k or count > c:
        ans += 1
        count, val = 1, i
print(ans)