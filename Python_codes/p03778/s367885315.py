W,a,b = map(int,input().split())
ans = max(a,b)-(min(a,b)+ W)

if ans <= 0:
    ans = 0
print(ans)