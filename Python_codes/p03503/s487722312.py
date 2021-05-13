def resolve():
    N = int(input())
    F = [int(input().replace(" ", ""), 2) for i in range(N)]
    P = [list(map(int, input().split(" "))) for i in range(N)]
    maxtotal = -1*float("inf")
    maxpattern = ""
    for bits in range(1, (1<<10)):
        total = 0
        for i in range(N):
            c = bin(bits & F[i]).count("1")
            total += P[i][c]
        if maxtotal < total:
            maxpattern = bits
            maxtotal = total
    print(maxtotal)




if '__main__' == __name__:
    resolve()