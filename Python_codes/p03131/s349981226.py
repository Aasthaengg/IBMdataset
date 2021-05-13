k,a,b = map(int,input().split())
ans = 1
if a+2 > b:
    ans += k
else:
    ans += min(k,a-1)
    k -= ans-1
    ans += k//2*(b-a)+k%2
print(ans)
