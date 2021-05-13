n= int(input())
a = list(map(int,input().split()))
ave = sum(a)/n
val = 10**4
for i in range(n):
    a[i] -= ave
    a[i] = abs(a[i])
    val = min(val,a[i])
ans = a.index(val)
print(ans)


