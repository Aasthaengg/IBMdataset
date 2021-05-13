n = int(input())
k = int(input())
x = int(input())
y = int(input())
ans = 0
if k>=n:
    ans += n*x 
else:
    ans += k*x + (n-k)*y
print(ans)