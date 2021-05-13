x,k,d = map(int,input().split())
y = abs(x)//d
if y >= k:
        ans = abs(abs(x)-d*k)

else:
        if (k-y)% 2 == 0:
                ans = abs(abs(x)-d*y)
        else:
                ans = min(abs(abs(x)-d*y+d),abs(abs(x)-d*y-d))
print(ans)