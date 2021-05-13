def main():
    n=int(input())
    g=[[] for _ in [0]*n]
    if n==3:
        print(2)
        print(1,3)
        print(2,3)
    elif n%2==0:
        print((n-2)*n//2)
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i+j!=n+1:
                    print(i,j)
    else:
        n-=1
        print((n*(n-2))//2+n)
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if i+j!=n+1:
                    print(i,j)
        for i in range(1,n+1):
            print(i,n+1)
main()