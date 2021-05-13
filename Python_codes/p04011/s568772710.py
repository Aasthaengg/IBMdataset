n = int(input())
k = int(input())
x = int(input())
y = int(input())

ans = 0
for i in range(1, n+1):
    if i >= k+1:
        ans += y
    else:
        ans += x
print(ans)
