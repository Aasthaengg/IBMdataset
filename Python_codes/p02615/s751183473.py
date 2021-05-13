n = int(input())

a = list(map(int, input().split()))
a.sort(reverse=True)

ans = a[0]

cnt = 1
i = 1
while cnt < n-1:
    cnt += 2
    ans += a[i] * 2
    i += 1

if cnt == n:
    ans -= a[i-1]

print(ans)    

