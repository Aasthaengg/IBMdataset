a,b,c,d = map(int,input().split())
ans = [a*c,a*d,b*c,b*d]
ans = sorted(ans)
print(ans[3])