S = input()
if len(S) == 26:
    done = set()
    for i, s in enumerate(S[::-1]):
        s = ord(s)
        if done:
            if max(done) < s:
                done.add(s)
                if i == 25:
                    print(-1)
            elif i != 25:
                l = 30
                for d in done:
                    if l > abs(d - s) and s < d:
                        x = d
                        l = d - s
                print(S[: -(i + 1)] + chr(x))
                break
            else:
                print(chr(ord(S[0]) + 1))
        else:
            done.add(s)
else:
    for i in range(ord("a"), ord("z") + 1):
        if not (chr(i) in S):
            print(S + chr(i))
            break