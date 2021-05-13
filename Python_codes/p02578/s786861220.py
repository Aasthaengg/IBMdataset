n = int(input())
L = list(map(int, input().split()))
m = 0
ans = 0
for l in L:
    m = max(m, l)
    ans += m - l
print(ans)