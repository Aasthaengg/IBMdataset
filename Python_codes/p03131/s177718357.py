k,a,b = map(int,input().split())
k -= a-1
div,mod = divmod(k,2)
ans = 1 + (a-1)
if a+2 <= b:
    dum = b-a
    ans += dum*div
    if mod == 1:
        ans += 1
else:
    ans += k
print(ans)