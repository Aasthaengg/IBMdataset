def make_divisors(n):
    if n==1:
        divisors=[1]
        return divisors
    else:
        divisors=[]
        for i in range(1,n):
            if i*i>n:
                break
            if n%i==0:
                divisors.append(i)
                if i!=n//i:
                    divisors.append(n//i)

        divisors.sort(reverse=True)
        return divisors

from sys import stdin
from math import gcd
def main():
    #入力
    readline=stdin.readline
    a,b,k=map(int,readline().split())

    c=gcd(a,b)
    li=make_divisors(c)

    print(li[k-1])

if __name__=="__main__":
    main()