n = int(input())
a = sorted(list(map(int,input().split())))
c0 = a.count(0)
ans = 'No'
if c0==n:
    ans = 'Yes'
if len(set(a))==2:
    c = a.count(a[-1])
    if c==n*2/3 and c0==n/3:
        ans = 'Yes'
if len(set(a))==3:
    s = 0
    f = True
    for i in set(a):
        s ^= i
        if a.count(i)!=n/3:
            f = False
    if f and s==0:ans='Yes'
print(ans)
