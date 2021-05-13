n = int(input())
l = list(map(int,input().split()))
r = list(map(int,input().split()))
l1 = max(l)
r1 = max(r)
left = 1
if l[0] == l1:left = 0

right = n-2
if r[-1] == l1:right = n-1

res = 1
if l1 != r1:print(0)
else:
    while l[left] != l1:
        if l[left] == l[left-1]:
            res = (res*l[left])%1000000007
        left += 1
    while r[right] != r1:
        if r[right] == r[right+1]:
            res = (res*r[right])%1000000007
        right -=1

    if  left > right:print(0)
    else:
        if  left < right:
            for i in range(right-left-1):
                res = (res*l1)%1000000007

        print(res%1000000007)


