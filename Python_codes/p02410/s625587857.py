def main():

    m, n = tuple(map(int, input().split()))
    a = [[0 for j in range(n)] for i in range(m)]
    b = [0 for j in range(n)]
    c = [0 for i in range(m)]

    for i in range(m):
        tmplst = list(map(int, input().split()))
        for j in range(n):
            a[i][j] = tmplst[j]

    for j in range(n):
        b[j] = int(input())

    for i in range(m):
        for j in range(n):
            c[i] += a[i][j] * b[j]
        print(c[i])



if __name__ == '__main__':
    main()
