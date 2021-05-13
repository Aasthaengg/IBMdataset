def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*n
    ma = a[0]
    mi = a[0]

    for i in range(1,n):
        if a[i] > ma:
            ma = a[i]
            b[i] = ma-mi
        if a[i] < mi:
            ma = a[i]
            mi = a[i]
    print(b.count(max(b)))

if __name__ == '__main__':
    main()
