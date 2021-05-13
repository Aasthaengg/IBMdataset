from sys import stdin
from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    t=[int(readline()) for _ in range(n)]

    ans=1
    for i in range(n):
        ans=lcm(ans,t[i])

    print(ans)

if __name__=="__main__":
    main()