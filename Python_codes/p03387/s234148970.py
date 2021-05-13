a,b,c = map(int,input().split())

s = a+b+c
m = max(a,b,c)

if s%2==m%2:
    ans = (3*m-s)//2
else:
    ans = (3*(m+1)-s)//2
    
print(ans)