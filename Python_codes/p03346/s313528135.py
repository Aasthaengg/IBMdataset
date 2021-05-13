def main():

    N = int(input())
    p = []
    for _ in range(N): p.append(int(input()))

    d = dict()
    for i in range(N):
        if i == 0:
            d[p[i]] = 1
        else:
            if p[i] - 1 in d:
                d[p[i]] = d[p[i]-1] + 1
            else:
                d[p[i]] = 1
    return N - max(list(d.values()))


if __name__ == '__main__':
    print(main())