n = int(input())
l = list(map(int, input().split(' ')))
mmin = l[0]
ans = 0
for i in range(n):
    if l[i] <= mmin:
        ans += 1
        mmin = l[i]
print(ans)