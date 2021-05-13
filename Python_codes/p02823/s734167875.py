n,a,b = map(int,input().split())
ans = (b-a)//2
if (b-a)%2!=0 and (a-1)<(n-b):
    ans += a
elif (b-a)%2!=0 and (a-1)>=(n-b):
    ans += n-b+1
print(ans)