n = int(input())
a = list(map(int,input().split()))
color = a[0]
ans = 0
for i in range(1,n):
    if color == a[i]:
        ans += 1
        color = 9999
    else:
        color = a[i]
print(ans)