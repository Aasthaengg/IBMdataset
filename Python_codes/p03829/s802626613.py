def main():
    n,a,b=map(int,input().split(' '))
    x=list(map(int,input().split(' ')))
    tmp = x[0]
    ans = 0
    for i in x[1:]:
        if a*(i - tmp) <=b:
            ans += a*(i-tmp)
        else:
            ans += b
        tmp = i
    print(ans)

if __name__ == '__main__':
    main()