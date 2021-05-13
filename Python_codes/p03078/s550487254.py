def resolve():
    X, Y, Z, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    AB = sorted(AB, reverse=True)[:K]
    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab+c)
    ABC = sorted(ABC, reverse=True)
    [print(ABC[i]) for i in range(K)]


if '__main__' == __name__:
    resolve()