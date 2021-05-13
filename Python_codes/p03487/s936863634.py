n = int(input())
a = list(map(int,input().split()))
a.sort()
a.append(-1)
ans = 0
p = 1
for i in range(1,n+1):
    if a[i-1] != a[i]:
        if a[i-1] != p:
            if p < a[i-1]:
                ans += p
            else:
                ans += p - a[i-1]
        p = 1
    else:
        p += 1
print(ans)