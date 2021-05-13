def main():
    h, w = map(int, input().split())
    a = [0]*26
    for i in range(h):
        s = input().rstrip()
        for c in s:
            a[ord(c) - ord("a")] += 1
    f = True
    for i in range(h//2):
        for j in range(w//2):
            sf = True
            for k in range(26):
                if a[k] >= 4:
                    a[k] -= 4
                    sf = False
                    break
            if sf:
                f = False
    if h%2 == 1:
        for j in range(w//2):
            sf = True
            for k in range(26):
                if a[k] >= 2:
                    a[k] -= 2
                    sf = False
                    break
            if sf:
                f = False
    if w%2 == 1:
        for i in range(h//2):
            sf = True
            for k in range(26):
                if a[k] >= 2:
                    a[k] -= 2
                    sf = False
                    break
            if sf:
                f = False
    if h%2 == 1 and w&2 == 1:
        sf = True
        for k in range(26):
            if a[k] >= 1:
                a[k] -= 1
                sf = False
                break
        if sf:
            f = False
    if f:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
