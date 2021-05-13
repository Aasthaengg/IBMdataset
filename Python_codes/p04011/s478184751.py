n,k,x,y = (int(input()) for i in[0]*4)
ans = 0
if n > k:
    ans = x*k + (n-k)*y
else:
    ans = n*x
print(ans)