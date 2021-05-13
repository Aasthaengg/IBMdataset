
def main():
    L = input()
    n = len(L)
    t = []
    mod = 10 ** 9 + 7
    for i, v in enumerate(L):
        if v == '1':
            t.append(i)
    r = 1
    p = 1
    for i, v in enumerate(reversed(L)):
        p %= mod
        if v == '1':
            r *= 2
            r += p
            r %= mod
        p *= 3
    print(r % mod)
main()
