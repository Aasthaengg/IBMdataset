def func(amat, bmat, nm):
    ans = [[0 for i in range(nm[2])] for j in range(nm[0])]
    for i in range(nm[0]):
        for j in range(nm[1]):
            for l in range(nm[2]):
                ans[i][l] += amat[i][j] * bmat[j][l]
    for i in ans:
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    nm = [int(i) for i in input().split(' ')]
    amat = [[0 for i in range(nm[1])] for j in range(nm[0])]
    bmat = [[0 for i in range(nm[2])] for i in range(nm[1])]

    for i in range(nm[0]):
        a = input().split(' ')
        for j in range(nm[1]):
            amat[i][j] = int(a[j])

    for i in range(nm[1]):
        b = input().split(' ')
        for j in range(nm[2]):
            bmat[i][j] = int(b[j])

    func(amat, bmat, nm)