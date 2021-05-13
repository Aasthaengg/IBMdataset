S = list(map(int, list(input())))

n = len(S)-1
for i in range(2 ** n):
    out = S[0]
    op = []
    for j in range(n):
        if (i>>j) & 1:
            out += S[j+1]
            op.append("+")
        else:
            out -= S[j+1]
            op.append("-")
    if out == 7:
        print(S[0], end='')
        for i in range(n):
            print(op[i], end='')
            print(S[i+1], end='')
        print("=7")
        exit()