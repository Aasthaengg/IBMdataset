MOD = 10**9+7
n = int(input())
a=[int(i) for i in input().split()]
tmp = 0
res = [0]*n
f=1
for i in a:
    tmp += f*i
    f=f*-1
res[0]=tmp
res[n-1] = 2*a[n-1]-res[0]
for i in range(n-2,0,-1):
    res[i] = 2*a[i]-res[i+1]

print(*res)
