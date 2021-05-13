from collections import Counter
def main():
    s = list(input())
    c = Counter(s)
    if len(s) != 26:
        for i in range(97, 123):
            if c[chr(i)] == 0:
                s.append(chr(i))
                print(''.join(s))
                exit()
            else:
                pass
    else:
        for i in range(1, 27):
            si = s[-i:]
            if si != sorted(si, reverse = True):
                ans = s[:-i]
                ans.append(min([sii for sii in si[1:] if sii > si[0]]))
                print(''.join(ans))
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()
