def agc034_b():
    s = str(input())
    n = len(s)
    if n < 3: return print(0)

    r = s[::-1]
    cb = 0
    ans = 0
    for i in range(1, n):
        if r[i] == 'A':
            if r[i-1] == 'C': cb = 0
            else: ans += cb
        elif r[i] == 'B':
            if r[i-1] == 'C': cb += 1
            else: cb = 0
        else:
            if r[i-1] == 'C': cb = 0
            else: continue
    print(ans)

if __name__ == '__main__':
    agc034_b()