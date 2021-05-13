# C - pushpush
n = int(input())
a = list(map(str,input().split()))

b = [""]*n
var = 0

if n % 2 == 0:
    for i in range(n):
        res = a[i]
        var += i*(-1)**i
        ind = n//2 + var
        b[ind] = res
else:
    for i in range(n):
        res = a[i]
        var += i*(-1)**i
        ind = n//2 - var
        b[ind] = res

ans = " ".join(b)
print(ans)
