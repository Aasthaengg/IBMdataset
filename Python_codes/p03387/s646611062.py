ls = list(map(int,input().split()))
ls.sort(reverse=True)
ans = 0
div1 = ls[0]-ls[1]
div2 = ls[1]-ls[2]
ans += div1
if div2 % 2== 0:
    ans += div2//2
else:
    ans += div2//2+2
print(ans)