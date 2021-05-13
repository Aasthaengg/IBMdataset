n = int(input())
a = list(map(int,input().split()))
for i in range(n-1):
    if a[i] > 0:
        pass
    else:
        a[i] *= -1
        a[i+1] *= -1
if a[-1] < 0:
    a[-1] *= -1
    a = sorted(a)
    ans = sum(a) - 2*a[0]
else:
    ans = sum(a)
print(ans)