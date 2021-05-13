def main() :
    n, q = [int(i) for i in input().split()]
    names = []
    times = []
    elapsed_time = 0
    for i in range(n) :
        inp = input().split()
        names.append(inp[0])
        times.append(int(inp[1]))


    while len(names) != 0 :
        if times[0] > q :
            tmp1 = names.pop(0)
            names.append(tmp1)
            tmp2 = times.pop(0) - q
            times.append(tmp2)
            elapsed_time += q
        else :
            tmp = names.pop(0)
            elapsed_time += times[0]
            times.pop(0)
            print(tmp, elapsed_time)


if __name__ == '__main__' :
    main()