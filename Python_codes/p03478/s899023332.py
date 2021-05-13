N,A,B = map(int,input().split())
ans = 0
def sumofdigits(X):
    s = str(X)
    t = list(map(int,s))
    return sum(t)
    
for i in range(1,N+1):
    if A <= sumofdigits(i) <= B:
        ans += i
print(ans)        
