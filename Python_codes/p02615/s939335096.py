n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = a[0]

j = 0
for i in range(1,n-1):
    if i % 2 == 1:
        j += 1
    ans += a[j]

print(ans)
