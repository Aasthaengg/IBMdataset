def ALDS1_3D():
    s0, s1 = [], []
    for i, e in enumerate(input()):
        if e == '\\':
                s0.append(i)
        elif e == '/':
            if len(s0) > 0:
                j = s0.pop()
                s = i - j
                while len(s1) > 0 and j < s1[-1][0]:
                    s += s1[-1][1]
                    s1.pop()
                s1.append((j, s))

    ss = [s[1] for s in s1]
    print(sum(ss))
    print(len(ss), *ss)





if __name__ == '__main__':
    ALDS1_3D()