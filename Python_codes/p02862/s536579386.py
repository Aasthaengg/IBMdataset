X, Y = map(int, input().split())

mod = 10**9+7
def factorial(N):
    if N==1 or N==1:
        return 1
    else:
        ans = N
        for i in range(1, N):
            ans*=N-i
            ans%=mod
        return ans

if 2*Y-X>=0 and (2*Y-X)%3==0 and 2*X-Y>=0 and (2*X-Y)%3==0:
    s = (2*X-Y)//3
    t = (2*Y-X)//3
    if s==0 and t==0:
        print(0)
    elif s==0:
        print(1)
    elif t==0:
        print(1)
    else:
        a = factorial(s+t)
        b = pow(factorial(s), mod-2, mod)
        c = pow(factorial(t), mod-2, mod)
        #print(a, b, c)
        print((a*b*c)%mod)
else:
    print(0)