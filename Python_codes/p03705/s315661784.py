n,a,b = list(map(int, input().split()))
ans = 0
if n==1 and a!=b:
    ans = 0
elif a>b:
    ans = 0
else:
    ans = ((n-1)*b + a) - ((n-1)*a + b) + 1
print(ans)