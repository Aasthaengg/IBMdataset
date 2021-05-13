from sys import stdin
from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    A=list(map(int,readline().split()))

    mod=10**9+7
    l=1
    for i in range(N):
        l=lcm(l,A[i])

    res=0
    for i in range(N):
        res+=l//A[i]
    
    print(res%mod)
if __name__=="__main__":
    main()