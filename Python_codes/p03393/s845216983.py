import string
def main():
    s = input()
    if len(s) < 26:
        print(s + sorted(list(set(string.ascii_lowercase) - set(s)))[0])
    else:
        t = []
        for i in range(len(s)):
            te = []
            for j in range(i+1, len(s)):
                if s[i] < s[j]: te.append(s[j])
            te.sort()
            t.append(te)
        for i in range(len(s)):
            if t[-1-i]:
                print(s[:-1-i] + t[-1-i][0])
                break
        else: print(-1)
    return

if __name__ == '__main__':
    main()
