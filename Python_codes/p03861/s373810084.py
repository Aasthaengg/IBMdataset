a,b,x = map(int,input().split())
ans = b//x - max(0,(a-1))//x
if a == 0:
    ans += 1
print(ans)