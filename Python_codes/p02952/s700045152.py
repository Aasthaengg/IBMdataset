n = int(input())
ans = 0
for i in range(1,n+1):
    x = str(i)
    if len(x) % 2 != 0:
        ans += 1
print(ans)