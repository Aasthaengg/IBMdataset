def main2():
    r = int(input())

    stick = [int(v) for v in input().split()]
    stick = sorted(stick, reverse=True)

    line = []
    tmp = -1
    for i in range(0, len(stick), 1):
        if tmp == stick[i]:
            line.append(stick[i])
            tmp = -1
        else:
            tmp = stick[i]
        if len(line) == 2:
            print(line[0] * line[1])
            exit()
    print(0)

main2()