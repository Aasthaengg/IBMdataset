n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
ans, now = a[0], 0
for i in range(1, n-1):
    if i%2 == 1:
        now += 1
    ans += a[now]
print(ans)
        

