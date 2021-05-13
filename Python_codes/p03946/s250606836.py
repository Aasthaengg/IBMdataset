n,t = map(int,input().split())
a= list(map(int,input().split()))

maxa = a[n-1]
sa = 0
res = 1
for i in range(n-1,-1,-1):
    if a[i] > maxa:
        maxa = a[i]
    tsa = maxa - a[i]
    if tsa > sa:
        sa = tsa
        res =1
    elif tsa == sa:
        res += 1

print(res)