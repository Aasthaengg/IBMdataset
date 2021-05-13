import itertools

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, K = ZZ()
    S = input()
    gr = itertools.groupby(S)
    ll = []
    for c, d in gr: ll.append([c, len(list(d))])

    output = N - len(ll)
    i = 1
    for _ in range(K):
        if i == len(ll)-1: output += 1
        elif i < len(ll): output += 2
        else: break
        i += 2

    print(output)

    return

if __name__ == '__main__':
    main()
