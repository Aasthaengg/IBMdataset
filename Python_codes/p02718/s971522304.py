n,m = map(int,input().split())
a = list(map(int, input().split()))
s = 0
for i in a:s+=i

ans = 0
for i in a:
    if(i >= s/(4*m)):
        ans+=1
if(ans >= m):print("Yes")
else:print("No")