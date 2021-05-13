import bisect

inf = 10**18

a,b,q = map(int,input().split())
s = [-inf]+[int(input()) for _ in range(a)]+[inf]
t = [-inf]+[int(input()) for _ in range(b)]+[inf]
x = [int(input()) for _ in range(q)]

for i in x:
    a1 = s[bisect.bisect_right(s,i)]
    b1 = t[bisect.bisect_right(t,i)]
    a2 = s[bisect.bisect_right(s,i)-1]
    b2 = t[bisect.bisect_right(t,i)-1]
    ans = inf
    for j in [a1,a2]:
        for k in [b1,b2]:
            ans = min(ans,abs(i-j)+abs(j-k),abs(i-k)+abs(k-j))
    print(ans)