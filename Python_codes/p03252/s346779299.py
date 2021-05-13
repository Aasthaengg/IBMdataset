def mi():
    return map(int, input().split())

def main():
    S = input()
    T = input()
    ds = {}
    dt = {}
    for i in range(len(S)):
        if not S[i] in ds:
            ds[S[i]] = 0
        if not T[i] in dt:
            dt[T[i]] = 0

        ds[S[i]] += 1
        dt[T[i]] += 1
    ls = sorted(list(ds.values()))
    lt = sorted(list(dt.values()))
    
    print('Yes' if ls == lt else 'No')


if __name__ == '__main__':
    main()