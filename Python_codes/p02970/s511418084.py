a,b=map(int,input().split())

ans = a//(2*b+1)

if a%(2*b+1) == 0: pass
else: ans += 1
print(ans)
