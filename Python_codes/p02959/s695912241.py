def main():
    n = int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]

    ind = 0
    res = 0

    for i in range(n):
        if a[i] <= b[i]:
            res += a[i]
            k = b[i]-a[i]
            res += min(k,a[i+1])

            a[i+1]=max(a[i+1]-k,0)

        else:
            res += b[i]
    print(res)



if __name__ == '__main__':
    main()
