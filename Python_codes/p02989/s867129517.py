def actual(n, D):
    D.sort()

    idx = int(len(D) // 2)
    abc_max = D[:idx][-1]
    arc_min = D[idx:][0]

    k = 0

    for i in range(abc_max + 1, arc_min + 1):
        k += 1

    return k

n = int(input())
D = list(map(int, input().split()))

print(actual(n, D))
