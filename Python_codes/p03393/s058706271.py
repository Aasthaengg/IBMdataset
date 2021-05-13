s = input()
alpha = list("abcdefghijklmnopqrstuvwxyz")
if len(s) != 26:
    for ss in s:
        alpha.remove(ss)
    print(s + alpha[0])
else:
    if s == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        tmp_pos = [[alpha.index(s[-1]), s[-1]]]
        for i, ss in enumerate(s[::-1], start = 1):
            for pos, tmp in tmp_pos:
                if alpha.index(ss) < pos:
                    print(s[:-i] + tmp)
                    exit()
            tmp = ss
            pos = alpha.index(ss)
            tmp_pos.append([pos, tmp])