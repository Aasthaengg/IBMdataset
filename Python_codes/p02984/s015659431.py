n = int(input())
a = list(map(int,input().split()))

su = 0
for i in range((n+1)//2):

    if i<(n-1)//2:
        su += (a[i]+a[n-i-1])*(-1)**i
    else:
        su += a[i]*(-1)**i

lis = [su]
for i in range(n-1):
    nex = 2*a[i]-lis[-1]
    lis.append(nex)

print(*lis)
