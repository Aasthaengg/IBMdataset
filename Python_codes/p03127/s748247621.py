n=int(input())
A=list(map(int,input().split()))
ans=A[0]
def gcd(a,b):
    if b==0: return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)

for i in range(n-1):
    ans=gcd(ans,A[i+1])
    if ans==1:
        print(1);exit()

print(ans)