def fact(n,mod):
    sm=1
    for i in range(2,n+1):
        sm*=i
        sm%=mod
    return sm

def main():
    mod=10**9+7
    x,y=map(int,input().split())
    if (x+y)%3!=0 : print(0);exit()
    times=(x+y)//3

    xwork,ywork=(x-times,y-times)

    if xwork<0 or ywork<0 : print(0);exit()

    sm=fact(times,mod)
    sm*=pow(fact(xwork,mod),mod-2,mod=mod)
    sm%=mod
    sm*=pow(fact(ywork,mod),mod-2,mod=mod)
    sm%=mod

    print(sm)

main()