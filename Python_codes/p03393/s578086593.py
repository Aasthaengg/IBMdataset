def main():
    S = input()
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    elif len(S) != 26:
        for i in range(26):
            a = chr(ord('a') + i)
            if a not in S:
                print(S + a)
                return
    else:
        while len(S) > 1:
            S = S[:-1]
            last = S[-1]
            while ord(last) < ord('z'):
                last = chr(ord(last) + 1)
                if last not in S:
                    print(S[:-1] + last)
                    return
if __name__ == '__main__':
    main()