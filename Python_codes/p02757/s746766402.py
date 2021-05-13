from collections import defaultdict
n,p = map(int,input().split())
s = list(map(int,list(input())))[::-1]
ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if s[i]%p==0:
            ans += n-i
    print(ans)
else:
    d = defaultdict(int)
    check = 0
    ten = 1
    for i in range(n):
        check += s[i]*ten
        check %= p
        ans += d[check]
        if check == 0:
            ans+=1
        d[check] += 1
        ten *= 10
        ten %= p
    print(ans)