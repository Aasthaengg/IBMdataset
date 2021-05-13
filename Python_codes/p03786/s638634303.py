n = int(input())
a = sorted(list(map(int, input().split())))

ans, val = 1, a[0]
for i in range(n-1):
    if val*2 >= a[i+1]:
        ans += 1
    else:
        ans = 1
    val += a[i+1]
print(ans)

