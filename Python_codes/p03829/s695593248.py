def main():
    n,a,b=map(int, input().split())
    x=[int(i) for i in input().split()]
    res=0
    for i in range(n-1):
        if((x[i+1]-x[i])*a > b):
            res+=b
        else:
            res+=((x[i+1]-x[i])*a)

    print(res)
if __name__ == '__main__':
    main()
