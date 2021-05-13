n, *a = map(int, open(0).read().split())
half_a = sum(a)//2
tmp = 0
for i in range(n):
    if tmp + a[i] >= half_a:
        ans1 = abs(tmp + a[i] - half_a) + abs(sum(a[i+1:]) - half_a)
        ans2 = abs(tmp - half_a) + abs(sum(a[i:]) - half_a)
        ans = min(ans1, ans2)
        break
    tmp += a[i]
print(ans)