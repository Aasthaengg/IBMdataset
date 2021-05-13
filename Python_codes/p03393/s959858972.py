def main():
    s = input()
    al = list("abcdefghijklmnopqrstuvwxyz")
    d = set(s)
    n = len(s)
    if list(s) == al[::-1]:
        print(-1)
        return 0
    if n == 26:
        for i in (range(n-1))[::-1]:
            if s[i] < s[i+1]:
                for j in range(i+1,n)[::-1]:
                    if s[i] < s[j]:
                        print(s[:i]+s[j])
                        return 0
    else:
        for i in al:
            if i not in d:
                print(''.join(s)+i)
                return 0

if __name__ == '__main__':
    main()
