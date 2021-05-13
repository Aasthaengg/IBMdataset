n = int(raw_input())
t = map(int, raw_input().split())
a = map(int, raw_input().split())
M = 10**9 + 7
ans = 1
m = [0] * n
if t[n-1] == a[0]:
    for i in xrange(n):
        if n == 1:
            break
        m = min([t[i], a[i]])
        flag1 = False
        flag2 = False
        if i > 0:
            if t[i-1] < t[i]:
                if a[i] < t[i]:
                    ans = 0
                    break
                flag1 = True
        else:
            flag1 = True
        if i < n-1:
            if a[i+1] < a[i]:
                if a[i] > t[i]:
                    ans  = 0
                    break
                flag2 = True
        else:
            flag2  = True
        #print m
        
        if not(flag1 or flag2):
            ans *= m
            ans %= M
else:
    ans = 0
print ans,