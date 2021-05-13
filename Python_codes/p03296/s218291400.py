n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 1
for i in range(1, n):
    if a[i-1] == a[i]: cnt += 1
    else:
        ans += cnt//2
        cnt = 1
ans += cnt//2
print(ans)