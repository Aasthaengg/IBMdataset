from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    h, w, k = map(int, input().split())
    s = [input() for _ in range(h)]
    st = [False] * h
    for i in range(h):
        if s[i].find('#') != -1:
            st[i] = True
    count = 0
    while st[count] == False:
        s[count] = list(s[i])
        count += 1
    c = 0
    for i in range(count, h):
        s[i] = list(s[i])
        fd = False
        if st[i] == False:
            s[i] = s[i-1]
            continue
        c += 1
        for j in range(w):
            if s[i][j] == '#':
                if fd == False:
                    fd = True
                    s[i][j] = c
                else:
                    c += 1
                    s[i][j] = c
            else:
                s[i][j] = c
    for i in range(count):
        s[i] = s[count]
    for i in range(h):
        for j in range(w):
            if j < w - 1:
                print(s[i][j], end=' ')
            else:
                print(s[i][j])


main()