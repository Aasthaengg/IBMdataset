n = int(input())

def g(x):
    return x*(x+1)//2

ans = 0
for k in range(1,n+1):
    ans += k*g(n//k)
print(ans)