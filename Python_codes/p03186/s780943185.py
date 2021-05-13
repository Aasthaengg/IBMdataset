def main():
    a,b,c=list(map(int,input().split()))
    if(a+b>=c):
        ans=b+c
    else:
        ans=a+2*b+1
    print(ans)

if __name__=="__main__":
    main()