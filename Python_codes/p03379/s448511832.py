def getval():
    n = int(input())
    x = list(map(int,input().split()))
    return n,x 

def main(n,x):
    y = sorted(x)
    a,b = y[(n-1)//2],y[(n-1)//2+1]
    for i in x:
        if i>a:
            print(a)
        else:
            print(b)

if __name__=="__main__":
    n,x = getval()
    main(n,x)