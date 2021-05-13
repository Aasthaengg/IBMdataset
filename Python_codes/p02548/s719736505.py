n = int(input())
n-=1
ans = 0
for x in range(1, n+1):
    ans += n//x
print(ans)