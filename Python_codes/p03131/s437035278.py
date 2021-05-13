import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    k,a,b=map(int, input().split())
    ans=0
    if b-1>a+1 and k>=a+1:
        k-=a+1
        ans+=b
        ans+=max(k//2*(b-a)+k%2,k//(a+2)*b+k%(a+2))
        print(ans)

    else:
        print(1+k)
resolve()