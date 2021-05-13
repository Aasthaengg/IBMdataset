from itertools import product
def main():
    s = list(input())
    koho = len(s) - 1
    pat = tuple(product(('+', ''), repeat = koho))
    r = 0
    for pate in pat:
        a = []
        for i, p in enumerate(pate):
            a.append(s[i])
            a.append(p)
        a.append(s[-1])
        r  += eval("".join(a))
    print(r)

if __name__ == '__main__':
    main()
