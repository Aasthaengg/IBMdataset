def main():
    k=int(input())
    n=50
    a=k%n
    w=k//n
    if k==0:
        print(2)
        print(1,1)
        return 0
    elif k==1:
        print(2)
        print(2,0)
        return 0
    elif k<n:
        print(k)
        print(*[k]*k)
        return 0
    print(n)
    p=[w+n-1]*n
    for i in range(a):
        p[i]=p[i]+n-a+1
    for i in range(a,n):
        p[i]-=a
    print(*p)
main()