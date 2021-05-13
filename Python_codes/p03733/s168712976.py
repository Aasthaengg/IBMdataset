def main():
    n,t = map(int,input().split())
    tl = list(map(int,input().split()))
    res = t
    for i in range(1,n):
        res += t - max((tl[i-1]+t-tl[i]),0)
    print(res)

if __name__ == '__main__':
    main()
