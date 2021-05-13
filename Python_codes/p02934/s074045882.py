n = int(input())
a = list(map(int,input().split()))
ans = 0
inv = 0
for i in range(0, n):
    inv = 1/a[i]
    ans += inv
ans = 1/ans
print(ans)