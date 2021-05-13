import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())

    ans=0
    i=0
    while ans<n:
        i+=1
        ans+=i

    print(i)
    rem=n-i
    i-=1
    if rem!=0:
        while i>0:

            if rem-i>=0:
                print(i)
                rem -=i
                i-=1
            else:
                i-=1


resolve()