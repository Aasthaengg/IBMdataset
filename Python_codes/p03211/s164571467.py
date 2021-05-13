def resolve():
    S = str(input())
    ls = []
    for i in range(len(S)-2):
        ls.append(S[i: i + 3])
    diff = []
    for l in ls:
        diff.append(abs(int(l) - 753))

    print(min(diff))

    return

resolve()