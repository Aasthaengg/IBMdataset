def main():
    H, W = (int(i) for i in input().split())
    A = [input() for i in range(H)]
    from collections import Counter
    c = Counter(A[0])
    for a in A[1:]:
        c += Counter(a)
    if H % 2 == 0 and W % 2 == 0:
        if all(v % 4 == 0 for v in c.values()):
            return print("Yes")
        else:
            return print("No")
    elif H % 2 == 1 and W % 2 == 1:
        c_odd = sum(1 if v % 2 == 1 else 0 for k, v in c.items())
        if c_odd == 1 and \
            sum(1 if v % 4 == 2 else 0 for v in c.values()) <= \
                (W//2 + H//2):
            return print("Yes")
        else:
            return print("No")
    else:
        if all(v % 2 == 0 for v in c.values()) and \
            sum(1 if v % 4 == 2 else 0 for v in c.values()) <= \
                (W//2 if W % 2 == 0 else H//2):
            return print("Yes")
        else:
            return print("No")


if __name__ == '__main__':
    main()
