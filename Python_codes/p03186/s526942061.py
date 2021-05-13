a,b,c = map(int, input().split())
if a+b < c: ans = b*2+a+1
elif a+b==c: ans = b*2+a
else: ans = b+c
print(ans)