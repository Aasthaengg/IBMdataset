n = int(input())
s = list(map(int,input().split()))
 
a = s[0]
b = sum(s)-a
ans = abs(a-b)
 
for i in range(1,n-1):
    a += s[i]
    b -= s[i]
    ans = min(ans,abs(a-b))
    
print(ans)