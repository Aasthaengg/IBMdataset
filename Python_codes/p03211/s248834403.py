x = list(map(int,input()))
ans = 2000
for i in range(2,len(x)):
    n = x[i-2]*100+x[i-1]*10+x[i]
    ans = min(ans,abs(n-753))
print(ans)
