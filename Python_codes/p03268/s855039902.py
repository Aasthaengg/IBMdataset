def main():
    n,k=map(int,input().split())
    if k%2==0:
        a=n//k
        print(a**3+(n//(k//2)-a)**3)
    else:
        print((n//k)**3)

if __name__ == '__main__':
    main()