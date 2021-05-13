N = int(input())
A = list(map(int,input().split()))

def gcd(x,y):
    if y==0: return x
    return gcd(y,x%y)
ans = A[0]
for a in A:
    ans = gcd(ans,a)
print(ans)