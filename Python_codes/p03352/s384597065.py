X = int(input())
maxx = int(X**(1/2))
ans = 1
for i in range(2,maxx+1):
    t = i
    while t <= X:
        ans = max(ans,t)
        t = t*i
print(ans)
