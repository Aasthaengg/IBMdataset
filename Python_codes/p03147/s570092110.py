n = int(input())
h = list(map(int, input().split()))
ans = 0
tmp = 0
for x in h:
    if tmp < x:
        ans += x - tmp
    tmp = x
print(ans)