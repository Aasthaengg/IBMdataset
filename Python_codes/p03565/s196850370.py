from copy import deepcopy
def main():
    s = list(input())
    t = list(input())
    tlen = len(t)
    kohos = []
    for i1 in range(len(s) - tlen + 1):
        s_range = s[i1:i1 + tlen]
        flag = 1
        for i2 in range(tlen):
            if s_range[i2] != '?' and s_range[i2] != t[i2]:
                flag = 0
        if flag:
            s_koho = deepcopy(s)
            s_koho[i1:i1 + tlen] = t
            kohos.append(s_koho)
    if kohos:
        kohos.sort()
        koho0 = deepcopy(kohos[0])
        koho0 = ['a' if c == '?' else c for c in koho0]
        r = "".join(koho0)
        print(r)
    else:
        print('UNRESTORABLE')

if __name__ == '__main__':
    main()
