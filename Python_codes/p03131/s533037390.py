k,a,b = map(int,input().split())
ans = 1
if b-a<2:
    ans += k
else:
    if k-(a-1)>0:
        k = k-(a-1)
        if k%2==0:ans = k//2*(b-a)+a
        else: ans = k//2*(b-a)+a+1
    else:
        ans += k
print(ans)