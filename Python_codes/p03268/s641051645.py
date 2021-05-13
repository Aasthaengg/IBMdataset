def main():
    n,k = map(int,input().split())
    if k%2==1:
        a=n//k
        print(a**3)
    else:
        a=n//k
        b=(n+k//2)//k
        print(a**3+b**3)

if __name__ == "__main__":
    main()