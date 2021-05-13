a,b,c = map(int,input().split())
if a+b<=c-1:
    ans = a+b+1+b
else:
    ans = b+c
print(ans)