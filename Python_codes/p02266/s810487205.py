def main():
    a = 0
    i = 0
    s = []
    u = []
    l = raw_input()
    for c in l:
        if c == '\\':
            s.append(i)
        elif c == '/' and len(s) > 0:
            j = s.pop()
            t = i - j
            a += t
            while len(u) > 0 and u[-1][0] > j:
                t += u.pop()[1]
            u.append((j, t))
        i += 1
    u.insert(0, (0, len(u)))

    print(a)
    print(' '.join(map(lambda x: str(x[1]), u)))


if __name__ == '__main__':
    main()