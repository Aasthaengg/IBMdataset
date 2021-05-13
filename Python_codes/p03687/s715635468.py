

def main():
    s = input()
    n = len(s)
    ans = 0
    for j in range(n):
        t = s
        cnt = 0
        for c in t:
            if c == s[j]:
                cnt += 1
        while len(t) != cnt:
            t2 = ''
            for i in range(len(t) - 1):
                t2 += (s[j] if s[j] == t[i] or s[j] == t[i + 1] else t[i])
            t = t2
            cnt = 0
            for c in t:
                if c == s[j]:
                    cnt += 1
        ans = max(ans, len(t))

    print(n - ans)



if __name__ == '__main__':
    main()
