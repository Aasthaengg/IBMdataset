def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    res = t
    for i in range(1,n):
        if a[i-1]+t <= a[i]:
            res += t
        else:
            res += t - (a[i-1]+t-a[i])
    print(res)

if __name__ == '__main__':
    main()
