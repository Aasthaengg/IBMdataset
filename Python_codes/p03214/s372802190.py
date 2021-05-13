n = int(input())
ls = list(map(int, input().split()))

ave = sum(ls) / n
mn = 101
ans = -1

for i in range(n):
    sa = abs(ls[i] - ave)
    if sa < mn:
        mn = sa
        ans = i

print(ans)