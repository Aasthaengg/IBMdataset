n,k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)

if k >= sum(a):
    print(0)
    exit()

def solve(time):
    cnt=0
    for i in range(n):
        tmp = time // f[i]
        if a[i] - tmp > 0:
            cnt += (a[i]-tmp)
    if cnt <= k:
        return True
    else:
        return False

r=0
l=0
for i in range(n):
    r=max(r,a[i]*f[i])

while r-l>1:
    mid=(l+r)//2

    if solve(mid):
        r=mid
    else:
        l=mid
print(r)