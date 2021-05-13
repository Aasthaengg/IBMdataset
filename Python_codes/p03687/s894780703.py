INF = 10 ** 8
def main():
    s = input()
    word = list(set(s))
    output = INF
    for c in word:
        t = s
        cnt = 0
        while len(set(t)) > 1:
            l = []
            for i in range(len(t)-1):
                if t[i] == c or t[i+1] == c: l.append(c)
                else: l.append(t[i])
            t = ''.join(l)
            cnt += 1
        output = min(output, cnt)
    print(output)
    return

if __name__ == '__main__':
    main()
