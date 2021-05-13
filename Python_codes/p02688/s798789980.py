def main():
    nk = [int(_x) for _x in input().split()]
    N = nk[0]
    K = nk[1]

    snuke = [True]*N

    for i in range(K):
        input()
        aa = [int(_x) for _x in input().split()]
        for a in aa:
            snuke[a-1] = False
    print(sum(snuke))


main()
