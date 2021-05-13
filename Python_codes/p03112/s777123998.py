from bisect import bisect_left as bl
a,b,q = map(int,input().split())

s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
s.insert(0,-10**12)
s.append(10**12)
t.insert(0,-10**12)
t.append(10**12)

for i in range(q):
    x = int(input())
    si = bl(s,x)
    ti = bl(t,x)
    ans = 10**12
    for j in range(si-1,si+1):
        for k in range(ti-1,ti+1):
            if s[j] <= t[k]:
                if t[k] <= x:
                    ans = min(ans,x-s[j])
                elif x <= s[j]:
                    ans = min(ans,t[k]-x)
                else:
                    ans = min(ans,min(x-s[j],t[k]-x)+t[k]-s[j])
            else:
                if s[j] <= x:
                    ans = min(ans,x-t[k])
                elif x <= t[k]:
                    ans = min(ans,s[j]-x)
                else:
                    ans = min(ans,min(x-t[k],s[j]-x)+s[j]-t[k])
    print(ans) 
