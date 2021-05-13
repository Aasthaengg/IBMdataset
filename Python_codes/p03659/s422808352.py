from sys import stdin
from itertools import accumulate
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    s1=list(accumulate(a))
    s2=list(accumulate(reversed(a)))

    ans=float("inf")
    for i in range(n-1):
        x=s1[i]
        y=s2[n-i-2]
        ans=min(ans,abs(x-y))

    print(ans)

if __name__=="__main__":
    main()