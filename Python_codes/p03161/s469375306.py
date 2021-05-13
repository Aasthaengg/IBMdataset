import math
n, k = map(int, input().split())
def better(l, ans, k):
    for i in range(2, n):
        #print(myarr(ans, k, i, l), ans)
        yy, xx = myarr(ans, k, i, l)
        ans[i] = min(func(yy, l[i], xx))
        #print(ans[i],func(yy, l[i], xx))
    return ans
def myarr(l, k, i, y):
    if i-k<0:
        return l[0:i], y[0:i]
    else:
        return l[(i-k):i], y[(i-k):i]
def func(l, i, xx):
    #print(l, xx, i)
    c = 0
    for a in l:
        #print(c)
        l[c]+=abs(i-xx[c])
        c+=1
    return l
l = list(map(int, input().split()))
ans = [0] * n
ans[1] = abs(l[1]-l[0])
print(better(l, ans, k)[len(ans)-1])