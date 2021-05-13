n = int(input())
ans = 10**9
for i in range(1,n//2+1):
    dum1 = n - i
    a = str(i)
    b = str(dum1)
    dum2 = 0
    for j in a:
        dum2 += int(j)
    for j in b:
        dum2 += int(j)
    ans = min(dum2,ans)
print(ans)