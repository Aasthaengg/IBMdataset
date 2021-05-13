import sys

n = int(input())
t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
if t[n-1]!=a[0]:
    print(0)
    sys.exit()

m =[]
for i in range(n):
    mx = min(t[i],a[i])
    mn = 1
    if i == 0:
        mn = t[i]
    elif i == n-1:
        mn = a[i]
    else :
        if t[i]!=t[i-1] :
            if t[i-1] > a[i-1]:
                print(0)
                exit()
            if mx == t[i]:
                mn=t[i]
        if a[i]!=a[i+1] :
            if a[i] > t[i]:
                print(0)
                exit()
            if mx == a[i]:
                mn=a[i]
    m.append([mx,min(mx,mn)])
ans = 1
for i in range(n):
    ans = (ans * (m[i][0]-m[i][1]+1))%(10**9+7)
print(ans)
