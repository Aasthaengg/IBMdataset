def main():
    N=int(input())
    for h in range(1,3501):
        for n in range(h,3501):
            a=4*h*n-N*(h+n)
            b=N*h*n
            if a>0 and b%a==0:
                print(h,n,b//a)
                return

if __name__ == "__main__":
    main()