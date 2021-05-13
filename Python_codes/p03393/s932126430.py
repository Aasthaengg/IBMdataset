def solve():
    S = input()

    if len(S) < 26:
        for a in [chr(ord("a")+i) for i in range(26)]:
            if a in S:
                continue
            print(S+a)
            return


    for i in range(26):
        for a in [chr(j) for j in range(ord(S[-1-i]), ord("z")+1)]:
            if a in S[:len(S)-i]:
                continue
            print(S[:len(S)-i-1]+a)
            return

    else:
        print(-1)

solve()