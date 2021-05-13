n = int(input())
lst = list(map(int, input().split()))
ans = 1
if 0 in lst:
    ans = 0
for i in range(n):
    ans *= lst[i]
    if ans > 10**18:
        ans = -1
        break
print(ans)