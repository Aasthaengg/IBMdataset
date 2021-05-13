def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    def n2(x):
        return x*(x+1)//2

    s = input()
    s +='.'
    ans = 0
    p = 0
    n = 0
    prev_p= 0
    for i in range(len(s)-1):
        if s[i] == '>':
            n += 1
            if s[i+1] == '<' or s[i+1] == '.':
                ans += n2(n)
                ans -= min(n, prev_p)
                n = 0
        else:
            p += 1
            if s[i+1] == '>':
                ans += n2(p)
                prev_p = p
                p = 0
            elif s[i+1] == '.':
                ans += n2(p)
                p = 0
    print(ans)




if __name__ == '__main__':
    main()