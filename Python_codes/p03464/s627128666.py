k = int(input())
a = list(map(int, input().split()))

def sim(num):
    for g in a:
        num = g * (num//g)
    return num

l=0
r=100+k*max(a)
while r-l>1:
    mid=(l+r)//2

    if sim(mid) > 2:
        r=mid
    else:
        l=mid
ans_max=l

l=0
r=100+k*max(a)
while r-l>1:
    mid=(l+r)//2

    if sim(mid) < 2:
        l=mid
    else:
        r=mid
ans_min=r

if ans_min > ans_max:
    print(-1)
else:
    print(ans_min,ans_max)