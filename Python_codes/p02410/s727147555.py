def func(amat, bmat, nm):
    for i in range(nm[0]):
        ans = 0
        for j in range(nm[1]):
            ans += amat[i][j] * bmat[j][0]
        print(ans)


if __name__ == '__main__':
    nm = input().split(' ')
    nm = [int(i) for i in nm]
    amat = [[0 for i in range(nm[1])] for j in range(nm[0])]
    bmat = [[0] for i in range(nm[1])]

    for i in range(nm[0]):
        a = input().split(' ')
        for j in range(nm[1]):
            amat[i][j] = int(a[j])

    for i in range(nm[1]):
        b = int(input())
        bmat[i][0] = b

    func(amat, bmat, nm)