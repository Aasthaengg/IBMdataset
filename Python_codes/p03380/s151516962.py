def getval():
    n = int(input())
    a = list(map(int,input().split()))
    return n,a

def main(n,a):
    a.sort()
    c = a[n-1]
    R = c/2
    r = 0
    for i in a:
        if abs(R-i)<abs(R-r):
            r = i 
    print("{x} {y}".format(x=c,y=r))

if __name__=="__main__":
    n,a = getval()
    main(n,a)