def main():
    S = input()
    wi = 0
    lo = 0
    g = 0
    p = 0
    for s in S:
        if s == "g":
            if p < g:
                p += 1
                wi += 1
            else:
                g += 1
        else:
            if p < g:
                p += 1
            else:
                g += 1
                lo += 1
    print(wi - lo)


if __name__ == '__main__':
    main()
