def resolve():
    n, m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    #+++
    xyz1 = []
    for i in range(n):
        xyz1.append(xyz[i][0] + xyz[i][1] + xyz[i][2])
    xyz1 = sorted(xyz1, reverse=True)
    sxyz1 = sum(xyz1[:m])

    #++-
    xyz2 = []
    for i in range(n):
        xyz2.append(xyz[i][0] + xyz[i][1] - xyz[i][2])
    xyz2 = sorted(xyz2, reverse=True)
    sxyz2 = sum(xyz2[:m])

    #+-+
    xyz3 = []
    for i in range(n):
        xyz3.append(xyz[i][0] - xyz[i][1] + xyz[i][2])
    xyz3 = sorted(xyz3, reverse=True)
    sxyz3 = sum(xyz3[:m])

    #+--
    xyz4 = []
    for i in range(n):
        xyz4.append(xyz[i][0] - xyz[i][1] - xyz[i][2])
    xyz4 = sorted(xyz4, reverse=True)
    sxyz4 = sum(xyz4[:m])

    # -++
    xyz5 = []
    for i in range(n):
        xyz5.append(-1*xyz[i][0] + xyz[i][1] + xyz[i][2])
    xyz5 = sorted(xyz5, reverse=True)
    sxyz5 = sum(xyz5[:m])

    # -+=
    xyz6 = []
    for i in range(n):
        xyz6.append(-1*xyz[i][0] + xyz[i][1] - xyz[i][2])
    xyz6 = sorted(xyz6, reverse=True)
    sxyz6 = sum(xyz6[:m])

    # --+
    xyz7 = []
    for i in range(n):
        xyz7.append(-1*xyz[i][0] - xyz[i][1] + xyz[i][2])
    xyz7 = sorted(xyz7, reverse=True)
    sxyz7 = sum(xyz7[:m])

    # ---
    xyz8 = []
    for i in range(n):
        xyz8.append(-1*xyz[i][0] - xyz[i][1] - xyz[i][2])
    xyz8 = sorted(xyz8, reverse=True)
    sxyz8 = sum(xyz8[:m])

    print(max(sxyz1, sxyz2, sxyz3, sxyz4, sxyz5, sxyz6, sxyz7, sxyz8))
resolve()