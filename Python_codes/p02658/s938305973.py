n = int(input())
x = [int(w) for w in input().split()]
x = sorted(x)
ans = 1
f = False
for i in range(n):
    ans *= x[i]
    if ans > 10**18:
        f = True
        break
    
if ans > 10**18:
    f = True
    
if(f):
    print(-1)
    
else:
    print(ans)