n = int(input())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

ans = 0
surplus = 0

for i in range(n) :
    tmp = min(a[i],surplus)
    ans += tmp
    a[i] -= tmp
    if b[i] > a[i] :
        ans += a[i]
        surplus = b[i] - a[i]
    else :
        ans += b[i]
        surplus = 0

tmp = min(a[n],surplus)
ans += tmp
print(ans)
