def main():
    S = input()
    gather = []
    beginR = 0
    state = 'R'
    for i in range(1, len(S)):
        if state == 'R':
            if S[i] == 'R':
                continue
            else:
                endR = i - 1
                beginL = i
                state = 'L'
        else:
            if S[i] == 'R':
                gather.append([beginR, endR, beginL, i-1], )
                beginR = i
                state = 'R'
            else:
                continue
    gather.append([beginR, endR, beginL, i])

    result = []
    for block in gather:
        r = block[:2]
        l = block[2:]
        rnum = r[1] - r[0] + 1
        lnum = l[1] - l[0] + 1

        for _ in range(rnum-1):
            result.append(0)

        if (rnum + lnum) % 2 == 0:
            for _ in range(2):
                result.append((rnum + lnum)//2)
        else:
            if rnum % 2 == 1:
                result.append((rnum + lnum)//2 + 1)
                result.append((rnum + lnum)//2)
            else:
                result.append((rnum + lnum)//2)
                result.append((rnum + lnum)//2 + 1)

        for _ in range(lnum-1):
            result.append(0)

    print(' '.join(map(str, result)))

main()