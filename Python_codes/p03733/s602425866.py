n,T = map(int,input().split())
t = [int(i) for i in input().split()]
ans = 0
for i in range(1,n) :
    x = t[i]-t[i-1]
    if x > T :
        ans += T
    else :
        ans += x

print(ans+T)