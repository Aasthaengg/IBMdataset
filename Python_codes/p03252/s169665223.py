
def main():
    S = list(input())
    T = list(input())
    d1 = {}
    d2 = {}
    for k in set(T):
        d1[k] = set()
    for k in set(S):
        d2[k] = set()
    for s, t in zip(S, T):
        d1[t].add(s)
        d2[s].add(t)
    if all([len(v) == 1 for v in d1.values()]) and all([len(v) == 1 for v in d2.values()]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
