N = int(input())
a = list(map(int,input().split()))
suma = sum(a)
sunuke = 0
arai = suma
for i in range(N-1):
    sunuke += a[i]
    arai -= a[i]
    sub = abs(sunuke - arai)
    if i == 0:
        ans = sub
    else:
        ans = min(ans,sub)
print(ans)
