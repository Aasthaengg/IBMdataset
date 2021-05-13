def main():
    N, M = (int(i) for i in input().split())
    PY = [([int(i) for i in input().split()], j) for j in range(M)]
    dic = {i: [] for i in range(N)}  # 県iの市を生まれた順に持つ
    A = sorted(PY, key=lambda p: p[0][1])
    for py, i in A:
        dic[py[0]-1].append(i)

    ans = []
    for p in range(N):  # 県ごとに番号を振る
        for x, i in enumerate(dic[p], start=1):
            # 県pの中でx番目に生まれた市i
            upper = "{:>06}".format(str(PY[i][0][0]))
            lower = "{:>06}".format(str(x))
            ans.append((upper+lower, i))
    ans.sort(key=lambda p: p[1])
    for a, _ in ans:
        print(a)


if __name__ == '__main__':
    main()
