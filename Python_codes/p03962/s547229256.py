a,b,c = map(int,input().split())
ans = 3
if a == b and b == c: ans = 1
elif a == b or b == c or a == c: ans = 2
print(ans)